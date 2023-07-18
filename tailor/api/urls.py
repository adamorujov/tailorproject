from django.urls import path
from tailor.api import views

urlpatterns = [
    path('settings-list/', views.SettingsListAPIView.as_view(), name="settings-list"),
    path('settings-update/<int:id>/', views.SettingsUpdateAPIView.as_view(), name="settings-update"),

    path('contactinformation-list/', views.ContactInformationListAPIView.as_view(), name="contactinformation-list"),
    path('contactinformation-create/', views.ContactInformationCreateAPIView.as_view(), name="contactinformation-create"),
    path('contactinformation-update-delete/<int:id>/', views.ContactInformationUpdateDestroyAPIView.as_view(), name="contactinformation-update-delete"),

    path('product-list/', views.ProductListAPIView.as_view(), name="product-list"),
    path('product-create/', views.ProductCreateAPIView.as_view(), name="product-create"),
    path('product-retrieve/<int:id>/', views.ProductRetrieveAPIView.as_view(), name="product-retrieve"),
    path('product-update-delete/<int:id>/', views.ProductRetrieveUpdateDestroyAPIView.as_view(), name="product-update-delete"),

    path('size-list/', views.SizeListAPIView.as_view(), name="size-list"),
    path('size-create/', views.SizeCreateAPIView.as_view(), name="size-create"),
    path('size-update-delete/<int:id>/', views.SizeRetrieveUpdateDestroyAPIView.as_view(), name="size-update-delete"),

    path('color-list/', views.ColorListAPIView.as_view(), name="color-list"),
    path('color-create/', views.ColorCreateAPIView.as_view(), name="color-create"),
    path('color-update-delete/<int:id>/', views.ColorRetrieveUpdateDestroyAPIView.as_view(), name="color-update-delete"),

    path('order-list/', views.OrderListAPIView.as_view(), name="order-list"),
    path('myorder/', views.CustomerOrderListAPIView.as_view(), name="myorder"),
    path('order-create/', views.OrderCreateAPIView.as_view(), name="order-create"),
    path('order-retrieve-update-delete/<int:id>/', views.OrderRetrieveUpdateDestroyAPIView.as_view(), name="order-retrieve-update-delete"),

    path('orderitem-list/', views.OrderItemListAPIView.as_view(), name="orderitem-list"),
    path('myorderitems/', views.OrderOrderItemListAPIView.as_view(), name="myorderitems"),
    path('orderitem-create/', views.OrderItemCreateAPIView.as_view(), name="orderitem-create"),
    path('orderitem-retrieve-update-delete/<int:id>/', views.OrderItemRetrieveUpdateDestroyAPIView.as_view(), name="orderitem-retrive-update-delete"),
]