from rest_framework.decorators import api_view
from apps.orders import services as svc
from apps.users.check_auth import permission
from apps.orders import schemas as schm


@schm.create_order_schema
@api_view(['POST'])
@permission(['USER'])
def create_order(request):
    return svc.OrderService(request).create_order()


@schm.update_order_schema
@api_view(['PUT'])
@permission(['OPERATOR'])
def update_order(request, pk):
    return svc.OrderService(request).update_order(pk)


@schm.get_orders_schema
@api_view(['GET'])
@permission(['OPERATOR'])
def get_orders(request):
    return svc.OrderService(request).get_orders()


@schm.get_user_orders_schema
@api_view(['GET'])
@permission(['USER'])
def get_user_orders(request):
    return svc.OrderService(request).get_user_orders()


@schm.get_user_order_schema
@api_view(['GET'])
@permission(['OPERATOR'])
def get_user_order(request, pk):
    return svc.OrderService(request).get_user_order(pk)
