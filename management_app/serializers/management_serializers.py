from rest_framework import serializers
from management_app.models import *
from django.db.transaction import atomic
from management_app.custom_helpers.model_serializers_helpers import comman_create_update_services, CustomExceptionHandler
from management_app.custom_helpers.consts import *
from management_app.custom_helpers.status_code import *


class HeadProductSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=True)
    category = serializers.CharField(required=True, max_length=100)
    price = serializers.FloatField(required=True)

    class Meta:
        model = Product
        exclude = ("status", "creation_date", "creation_by", "updation_date", "updation_by",)
    
    
    def validate(self, data):
        data = super().validate(data)
        return {key: value for key, value in data.items() if value is not None}
    
    def validate_price(self, value):
        if value < 0:
            raise CustomExceptionHandler("Price should be greater than 0")
        return value
    
    def to_representation(self, data):
        data = super().to_representation(data)
        return data
    
    @atomic
    def create(self, validated_data):
        return comman_create_update_services(self, validated_data)

    @atomic
    def update(self, instance, validated_data):
        return comman_create_update_services(self, validated_data, instance)

# create update Product

class ProductRequestSerializer(serializers.ModelSerializer):

    products = HeadProductSerializer(many=True,required=False)

    class Meta:
        model = Product
        fields = ("products",)

class ProductReponseSerializer(serializers.ModelSerializer):
    
    status = serializers.IntegerField(help_text = "Status Code", required = False)
    message = serializers.CharField(help_text = "Status Message", required = False)
    data = HeadProductSerializer(required=False, many=True)

    class Meta:
        model = Product
        fields = ("status", "message", "data",)

# Delete Product

class ProductDeleteRequestSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=True)

    class Meta:
        model = Product
        fields = ("id",)


class ProductDeleteResponseSerializer(serializers.ModelSerializer):

    status = serializers.IntegerField(help_text = "Status Code", required = False)
    message = serializers.CharField(help_text = "Status Message", required = False)

    class Meta:
        model = Product
        fields = ("status", "message",)


# Get Product

class GetProductRequestSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)

    class Meta:
        model = Product
        fields = ("id",)


class GetProductResponseSerializer(serializers.ModelSerializer):
    
    status = serializers.IntegerField(help_text = "Status Code", required = False)
    message = serializers.CharField(help_text = "Status Message", required = False)
    data = HeadProductSerializer(required=False, many=True)

    class Meta:
        model = Product
        fields = ("status", "message", "data",)


