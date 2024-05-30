from django.db import models
from management_app.custom_helpers.model_serializers_helpers import AddCommonField


class CommonProduct(AddCommonField):

    id = models.BigAutoField(primary_key=True) 
    name = models.TextField(null=False)
    category = models.CharField(null=False, max_length=100)
    price = models.FloatField(null=False)

    class Meta:
        abstract = True

class Product(CommonProduct):

    class Meta:
        db_table = "pm_product"
        ordering = ('-creation_date',)
