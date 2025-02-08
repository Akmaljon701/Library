from drf_spectacular.utils import extend_schema

from apps.orders import serializers
from utils.exceptions import resp


create_order_schema = extend_schema(
    summary='Create Order',
    request=serializers.OrderCreateSerializer(),
    responses=resp(201)
)

update_order_schema = extend_schema(
    summary='Update Order',
    request=serializers.OrderUpdateSerializer(),
    responses=resp(200)
)

get_orders_schema = extend_schema(
    summary='Orders',
    request=None,
    responses=resp(200, serializers.OrderSerializer)
)

get_user_orders_schema = extend_schema(
    summary="User's Orders",
    request=None,
    responses=resp(200, serializers.OrderSerializer)
)

get_user_order_schema = extend_schema(
    summary="User Orders",
    request=None,
    responses=resp(200, serializers.OrderSerializer)
)
