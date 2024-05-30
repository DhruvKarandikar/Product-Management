from management_app.models import *
from management_app.serializers.management_serializers import HeadProductSerializer
from management_app.custom_helpers.status_code import *
from management_app.custom_helpers.model_serializers_helpers import CustomExceptionHandler, create_update_model_serializer

def product_create_service(request_data):
    product_instances = request_data.pop('products', [])

    final_data = []

    if request_data is None or request_data == {}:
        raise CustomExceptionHandler(request_data_empty)

    for product in product_instances:
        product_instance = create_update_model_serializer(HeadProductSerializer, product, partial=True)
        final_data.append(product_instance)

    product_serializer_objs = HeadProductSerializer(final_data, many=True).data

    return get_response(success, data={"data": product_serializer_objs})



def product_delete_service(request_data):
    req_id = request_data.get('id', None)
    query_obj = None

    if not req_id:
        raise CustomExceptionHandler(no_object_exist)

    query_obj = Product.objects.filter(id=req_id).first()
    query_obj.status = 0
    query_obj.save()

    return get_response(success)


def get_product_service(request_data):
    req_id = request_data.get('id', None)
    query_obj = []

    if req_id:
        query_obj = Product.objects.filter(id=req_id, status=STATUS_ACTIVE)
    else:
        query_obj = Product.objects.filter(status=STATUS_ACTIVE)

    serializer_obj = HeadProductSerializer(query_obj, many=True).data
    return get_response(success, data=serializer_obj)
