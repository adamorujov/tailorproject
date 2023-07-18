from django.contrib import admin, messages
from tailor.models import (
    SettingsModel, ContactInformationModel, SizeModel, ProductModel, ColorModel,
    OrderModel, OrderItemModel
    )
from django.utils.translation import gettext_lazy

admin.site.register(SettingsModel)
admin.site.register(ContactInformationModel)
admin.site.register(SizeModel)
admin.site.register(ColorModel)

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("__str__", "price", "sale_price")

class OrderItemAdmin(admin.TabularInline):
    model = OrderItemModel
    extra = 3

@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("__str__", "status")
    list_filter = ("status",)
    search_fields = ('first_name', 'last_name', 'email')
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

