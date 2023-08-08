from rest_framework import serializers
from tailor.models import (
    SettingsModel, ContactInformationModel, ProductModel, SizeModel, ColorModel,
    OrderModel, OrderItemModel, CategoryModel, ProductImageModel, FavouriteModel
)
from account.api.serializers import CustomerSerializer

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingsModel
        fields = "__all__"

class ContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformationModel
        fields = "__all__"

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeModel
        fields = "__all__"

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorModel
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageModel
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    sizes = SizeSerializer(many=True)
    colors = ColorSerializer(many=True)
    categories = CategorySerializer(many=True)
    product_images = ProductImageSerializer(many=True)
    class Meta:
        model = ProductModel
        fields = "__all__"

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    user = CustomerSerializer()

    class Meta:
        model = OrderModel
        fields = "__all__"

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        exclude = ("status",)

class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    product = ProductSerializer()

    class Meta:
        model = OrderItemModel
        fields = "__all__"

class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItemModel
        fields = "__all__"

class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteModel
        fields = "__all__"

        