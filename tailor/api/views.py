from rest_framework.generics import (
    ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView,
    RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from tailor.models import (
    SettingsModel, ContactInformationModel, ProductModel, SizeModel, ColorModel,
    OrderModel, OrderItemModel, CategoryModel, ProductImageModel, FavouriteModel
)
from tailor.api.serializers import (
    SettingsSerializer, ContactInformationSerializer, ProductSerializer, SizeSerializer,
    ProductCreateSerializer, ColorSerializer,
    OrderSerializer, OrderCreateSerializer, OrderItemSerializer, OrderItemCreateSerializer,
    CategorySerializer, ProductImageSerializer, FavouriteSerializer
)


# -------- Settings API Views ---------

class SettingsListAPIView(ListAPIView):
    queryset = SettingsModel.objects.all()
    serializer_class = SettingsSerializer

class SettingsUpdateAPIView(RetrieveUpdateAPIView):
    queryset = SettingsModel.objects.all()
    serializer_class = SettingsSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = "id"


# -------- ContactInformation API Views -----------

class ContactInformationListAPIView(ListAPIView):
    queryset = ContactInformationModel.objects.all()
    serializer_class = ContactInformationSerializer

class ContactInformationCreateAPIView(CreateAPIView):
    queryset = ContactInformationModel.objects.all()
    serializer_class = ContactInformationSerializer
    permission_classes = (IsAdminUser,)

class ContactInformationUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ContactInformationModel.objects.all()
    serializer_class = ContactInformationSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = "id"


# --------- Product API Views -----------

class ProductListAPIView(ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    
class ProductCreateAPIView(CreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = (IsAdminUser,)

class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"

class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = (IsAdminUser, )
    lookup_field = "id"

# --------- Size API View ----------

class SizeListAPIView(ListAPIView):
    queryset = SizeModel.objects.all()
    serializer_class = SizeSerializer

class SizeCreateAPIView(CreateAPIView):
    queryset = SizeModel.objects.all()
    serializer_class = SizeSerializer
    permission_classes = (IsAdminUser,)

class SizeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SizeModel.objects.all()
    serializer_class = SizeSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = "id"

# ----------- Color API View ------------

class ColorListAPIView(ListAPIView):
    queryset = ColorModel.objects.all()
    serializer_class = ColorSerializer

class ColorCreateAPIView(CreateAPIView):
    queryset = ColorModel.objects.all()
    serializer_class = ColorSerializer
    permission_classes = (IsAdminUser,)

class ColorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ColorModel.objects.all()
    serializer_class = ColorSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = "id"

# ---------- Order API View -----------
class OrderListAPIView(ListAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminUser,)

class CustomerOrderListAPIView(ListAPIView):
    def get_queryset(self):
        return OrderModel.objects.filter(user=self.request.user)
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

class OrderCreateAPIView(CreateAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderItemCreateSerializer

class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderCreateSerializer
    lookup_field = "id"

# -------- Order Item API View ----------

class OrderItemListAPIView(ListAPIView):
    queryset = OrderItemModel.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = (IsAdminUser,)

class OrderOrderItemListAPIView(ListAPIView):
    def get_queryset(self):
        return OrderItemModel.objects.filter(
            order__user = self.request.user
        )
    serializer_class = OrderItemSerializer
    permission_classes = (IsAuthenticated,)

class OrderItemCreateAPIView(CreateAPIView):
    queryset = OrderItemModel
    serializer_class = OrderItemCreateSerializer

class OrderItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = OrderItemModel
    serializer_class = OrderItemCreateSerializer
    lookup_field = "id"

# ----------- Category API View ----------
class CategoryListAPIView(ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

class CategoryCreateAPIView(CreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"

# --------- Product Image API View ----------
class ProductImageListAPIView(ListAPIView):
    queryset = ProductImageModel.objects.all()
    serializer_class = ProductImageSerializer

class ProductImageCreateAPIView(CreateAPIView):
    queryset = ProductImageModel.objects.all()
    serializer_class = ProductImageSerializer

class ProductImageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ProductImageModel.objects.all()
    serializer_class = ProductImageSerializer
    lookup_field = "id"

# ---------- Favourite API View --------
class FavouriteListAPIView(ListAPIView):
    queryset = FavouriteModel.objects.all()
    serializer_class = FavouriteSerializer

class CustomerFavouriteListAPIView(ListAPIView):
    def get_queryset(self):
        return FavouriteModel.objects.filter(user=self.request.user)
    serializer_class = FavouriteSerializer
    permission_classes = (IsAuthenticated,)

class FavouriteCreateAPIView(CreateAPIView):
    queryset = FavouriteModel.objects.all()
    serializer_class = FavouriteSerializer

class FavouriteRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = FavouriteModel.objects.all()
    serializer_class = FavouriteSerializer
    lookup_field = "id"