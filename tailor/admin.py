from django.contrib import admin
from tailor.models import SettingsModel, ContactInformationModel, SizeModel, ProductModel, ColorModel

admin.site.register(SettingsModel)
admin.site.register(ContactInformationModel)
admin.site.register(SizeModel)
admin.site.register(ProductModel)
admin.site.register(ColorModel)
