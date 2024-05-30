import json
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from management_app.custom_helpers.status_code import get_response, generic_error_2
from management_app.custom_helpers.model_serializers_helpers import CustomExceptionHandler
from management_app.serializers.management_serializers import *
from management_app.services.management_services import product_create_service, product_delete_service, get_product_service
from management_app.custom_helpers.custom_decorator import custom_api_view

logger = logging.getLogger("django")


@csrf_exempt
@swagger_auto_schema(
    methods=['post'],
    request_body=ProductRequestSerializer,
    responses={"200": ProductReponseSerializer},
    operation_id="Product Create Update"
)
@api_view(["POST"])
def product_create_update(request):
    response_obj = None

    try:
        logger.info(request, "request for product crud")
        response_obj = product_create_service(request.data)

    except CustomExceptionHandler as e:
        logger.exception(f"Custom Exception in product crud: {e}")
        response_obj = get_response(eval(str(e)))

    except Exception as e:
        logger.exception(f"Exception in product crud {e}")
        response_obj = get_response(generic_error_2)

    logger.info("response in product crud --> %s", response_obj)
    return JsonResponse(response_obj, safe=False)


@csrf_exempt
@custom_api_view(
    request_serializer=ProductDeleteRequestSerializer,
    responses={"200": ProductDeleteResponseSerializer},
    operation_id="Delete Product"
)
def delete_product(request):
    response_obj = None

    try:
        logger.info(request, "request for delete product")
        response_obj = product_delete_service(request.validation_serializer.validated_data)

    except CustomExceptionHandler as e:
        logger.exception(f"Custom Exception in delete product url: {e}")
        response_obj = get_response(eval(str(e)))

    except Exception as e:
        logger.exception(f"Exception in delete product url {e}")
        response_obj = get_response(generic_error_2)

    logger.info("response in delete product --> %s", response_obj)
    return JsonResponse(response_obj, safe=False)

@csrf_exempt
@custom_api_view(
    request_serializer=GetProductRequestSerializer,
    responses={"200": GetProductResponseSerializer},
    operation_id="Get Product"
)
def get_product(request):
    response_obj = None

    try:
        logger.info(request, "request for get product")
        response_obj = get_product_service(request.validation_serializer.validated_data)

    except CustomExceptionHandler as e:
        logger.exception(f"Custom Exception in get product url: {e}")
        response_obj = get_response(eval(str(e)))

    except Exception as e:
        logger.exception(f"Exception in get product url {e}")
        response_obj = get_response(generic_error_2)

    logger.info("response in get product --> %s", response_obj)

    return JsonResponse(response_obj, safe=False)

