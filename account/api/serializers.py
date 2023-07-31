from rest_framework import serializers
from account.models import Customer, Message
from django.contrib.auth.password_validation import validate_password

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class CustomerCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'password')

    def validate(self, data):
        validate_password(data["password"])
        return data

    def create(self, validated_data):
        account = Customer.objects.create(
            email = validated_data["email"],
        )
        account.set_password(validated_data["password"])
        account.save()
        return account

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"