from django.db import models
from account.models import Customer
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

from django.utils.functional import lazy

class SettingsModel(models.Model):
    logo = models.ImageField("Loqo", upload_to="logo/", blank=True, null=True)
    banner_image = models.ImageField("Banner şəkli", upload_to="banner_image/", blank=True, null=True)
    banner_title = models.CharField("Banner başlığı", max_length=256, blank=True, null=True)
    about_us = models.TextField("Haqqımızda", blank=True, null=True)

    class Meta:
        verbose_name = "Parametr"
        verbose_name_plural = "Parametrlər"

    def __str__(self)-> str:
        return "Parametrlər"
    
class ContactInformationModel(models.Model):
    address = models.TextField("Ünvan", blank=True, null=True)
    contact_number = models.CharField("Əlaqə nömrəsi", max_length=50, blank=True, null=True)
    email = models.EmailField("Email", max_length=256, blank=True, null=True)

    class Meta:
        verbose_name = "Əlaqə məlumatı"
        verbose_name_plural = "Əlaqə məlumatları"

    def __str__(self) -> str:
        contact_informations = ContactInformationModel.objects.all()
        return "Əlaqə məlumatı " + str(list(contact_informations).index(self) + 1)
    
class SizeModel(models.Model):
    size = models.CharField("Ölçü", max_length=10)

    class Meta:
        verbose_name = "Ölçü"
        verbose_name_plural = "Ölçülər"

    def __str__(self) -> str:
        return self.size
    
class ColorModel(models.Model):
    color = models.CharField("Rəng", max_length=50)
    color_code = models.CharField("Rəng kodu", max_length=10)

    class Meta:
        verbose_name = "Rəng"
        verbose_name_plural = "Rənglər"

    def __str__(self):
        return self.color
    
class CategoryModel(models.Model):
    name = models.CharField(verbose_name="Ad", max_length=528)

    class Meta:
        verbose_name = "Kateqoriya"
        verbose_name_plural = "Kateqoriyalar"
        ordering = ("-id", )

    def __str__(self):
        return self.name
    
class ProductModel(models.Model):
    image = models.ImageField("Şəkil", upload_to="product_images/", blank=True, null=True)
    title = models.CharField("Başlıq", max_length=512)
    price = models.FloatField("Qiymət", default=0)
    sale_price = models.FloatField("Endirimli qiymət", blank=True, null=True)
    sizes = models.ManyToManyField(SizeModel, verbose_name="Ölçülər", blank=True, related_name="size_products")
    colors = models.ManyToManyField(ColorModel, verbose_name="Rənglər", blank=True, related_name="color_products")
    characteristics = RichTextField(verbose_name="Xarakteristika", blank=True, null=True)
    note = RichTextField(verbose_name="Qeyd", blank=True, null=True)
    categories = models.ManyToManyField(CategoryModel, blank=True, related_name="category_products")


    def img_preview(self): #new
        return mark_safe(f'<img src = "{self.image.url}" width = "20" />')
    
    def show_price(self):
        return mark_safe(f'<b>{self.price} AZN</b>')
    
    def show_sale_price(self):
        return mark_safe(f'<b>{self.sale_price} AZN</b>')

    class Meta:
        verbose_name = "Məhsul"
        verbose_name_plural = "Məhsullar"
        ordering = ("-id",)

    def __str__(self) -> str:
        return self.title

class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to="product_images/")

    class Meta:
        verbose_name = "Məhsul şəkli"
        verbose_name_plural = "Məhsul şəkilləri"
        ordering = ("-id",)

    def __str__(self):
        return self.image.url
    
    def img_preview(self):
        return mark_safe(f"<img src='{self.image.url}' width='20'/>")
    
class OrderModel(models.Model):
    STATUS = [
        ("C", "Çatdırılıb"),
        ("CM", "Çatdırılmayıb"),
    ]
    user = models.OneToOneField(Customer, verbose_name="İstifadəçi", on_delete=models.CASCADE, related_name="order", blank=True, null=True)
    first_name = models.CharField("Ad", max_length=100, blank=True, null=True)
    last_name = models.CharField("Soyad", max_length=100, blank=True, null=True)
    email = models.EmailField("Email", max_length=256, blank=True, null=True)
    phone_number = models.CharField("Əlaqə nömrəsi", max_length=50, blank=True, null=True)
    address = models.TextField("Ünvan")
    note = models.TextField("Qeyd", blank=True, null=True)
    status = models.CharField("Status", max_length=2, choices=STATUS, default="CM")

    class Meta:
        verbose_name = "Sifarişçi"
        verbose_name_plural = lazy(lambda: _("Sifarişçilər ({})").format(OrderModel.objects.filter(status="CM").count()), str)()

    def Email(self):
        return mark_safe(f"<b>{self.email}</b>") if self.status == "CM" else mark_safe(f"{self.email}")
    
    def Status(self):
        return mark_safe(f"<b>Çatdırılmayıb</b>") if self.status == "CM" else mark_safe(f"Çatdırılıb")

    def save(self, *args, **kwargs):
        if self.user:
            self.first_name = self.user.first_name
            self.last_name = self.user.last_name
            self.email = self.user.email
            self.phone_number = self.user.phone_number
        return super(OrderModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.email


class OrderItemModel(models.Model):
    product = models.ForeignKey(ProductModel, verbose_name="Məhsul", on_delete=models.CASCADE, related_name="product_orderitems")
    order = models.ForeignKey(OrderModel, verbose_name="Sifariş", on_delete=models.CASCADE, related_name="order_orderitems")
    quantity = models.IntegerField("Miqdar", default=0)
    color = models.CharField("Rəng", max_length=100, blank=True, null=True)
    size = models.CharField("Ölçü", max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Sifariş edilən"
        verbose_name_plural = "Sifariş edilənlər"
        ordering = ("-id",)

    def __str__(self):
        return self.product.title + " x " + str(self.quantity)
    

class FavouriteModel(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="user_favourites")
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="product_favourites")

    class Meta:
        verbose_name = "Favorit"
        verbose_name_plural = "Favoritlər"
        ordering = ("-id",)

    def __str__(self):
        return self.user.username + " | " + self.product.title
    
