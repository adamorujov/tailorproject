from django.contrib import admin, messages
from django.http.request import HttpRequest
from tailor.models import (
    SettingsModel, ContactInformationModel, SizeModel, 
    ProductModel, ProductImageModel, ColorModel,
    OrderModel, OrderItemModel, CategoryModel, FavouriteModel
    )
from django.utils.translation import gettext_lazy

# from django.contrib.admin.sites import AdminSite

# AdminSite.site_header = 'Techmasoft administrasiyası'
# AdminSite.site_title = 'Techmasoft sayt administratoru'

admin.site.register(ContactInformationModel)
admin.site.register(SizeModel)
admin.site.register(ColorModel)
admin.site.register(CategoryModel)
admin.site.register(FavouriteModel)

@admin.register(SettingsModel)
class SettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request: HttpRequest) -> bool:
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


class ProductImageAdmin(admin.TabularInline):
    model = ProductImageModel
    extra = 3

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("__str__", "show_price", "show_sale_price", "img_preview")
    list_display_links = ("__str__", "img_preview")

    inlines = [ProductImageAdmin]


class OrderItemAdmin(admin.TabularInline):
    model = OrderItemModel
    readonly_fields = ('product', 'order', 'quantity', 'color', 'size')
    extra = 0

@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("Email", "Status")
    list_filter = ("status",)
    search_fields = ('first_name', 'last_name', 'email')
    readonly_fields = ('user', 'first_name', 'last_name', 
                       'email', 'phone_number', 'address',
                       'note',
                    )
    inlines = [OrderItemAdmin]
    actions = ['mark_in_c', 'mark_in_cm']

    @admin.action(description="Sifariş çatdırıldı")
    def mark_in_c(self, request, queryset):
        updated = queryset.update(status="C")
        self.message_user(request, "Seçilmiş sifarişlər çatdırıldı.", messages.SUCCESS)

    @admin.action(description="Sifariş çatdırılmadı")
    def mark_in_cm(self, request, queryset):
        updated = queryset.update(status="CM")
        self.message_user(request, ("Seçilmiş sifarişlər çatdırılmadı."), messages.SUCCESS)
