from django.urls import path
from account.api import views

urlpatterns = [
    path('user-list/', views.CustomerListAPIView.as_view(), name="users"),
    path('user-create/', views.CustomerCreateAPIView.as_view(), name="user-create"),
    path('user-retrieve-update-delete/<int:id>/', views.CustomerRetrieveUpdateDestroyAPIView.as_view(), name="user-retrieve-update-delete"),

    path('message-list/', views.MessageListAPIView.as_view(), name="message-list"),
    path('message-create/', views.MessageCreateAPIView.as_view(), name="message-create"),
    path('message-retrieve/<int:id>/', views.MessageRetrieveAPIView.as_view(), name="message-retrieve"),
    path('message-delete/<int:id>/', views.MessageDeleteAPIView.as_view(), name="message-delete"),
]