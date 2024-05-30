from django.urls import path
from management_app.views import *

urlpatterns = [
    path('management_app/product', product_create_update, name='product_crud'),
    path('management_app/product_delete', delete_product, name='product_delete'),
    path('management_app/get_product', get_product, name='get_product'),
]

