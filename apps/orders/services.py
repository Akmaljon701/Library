from rest_framework.response import Response

from utils.exceptions import raise_error, ErrorCodes
from utils.pagination import BaseService, BaseServicePagination
from apps.orders import models as orders_models
from apps.orders import serializers


class OrderService(BaseServicePagination):

    def create_order(self):
        serializer = serializers.OrderCreateSerializer(
            data=self.request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=201)

    def update_order(self, pk):
        serializer = serializers.OrderUpdateSerializer(
            self._get_order(pk),
            data=self.request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=200)

    def get_orders(self):
        orders = orders_models.Order.objects.all()
        results = self.paginate(orders)
        serializer = serializers.OrderSerializer(
            results,
            many=True
        )
        return self.paginated_response(serializer.data)

    def get_user_orders(self):
        orders = orders_models.Order.objects.filter(
            user=self.request.user
        ).all()
        results = self.paginate(orders)
        serializer = serializers.OrderSerializer(
            results,
            many=True
        )
        return self.paginated_response(serializer.data)

    def get_user_order(self, pk):
        orders = orders_models.Order.objects.filter(
            id=pk,
            user=self.request.user
        ).all()
        results = self.paginate(orders)
        serializer = serializers.OrderSerializer(
            results,
            many=True
        )
        return self.paginated_response(serializer.data)

    def _get_order(self, pk):
        try:
            order = orders_models.Order.objects.get(id=pk)
        except orders_models.Order.DoesNotExist:
            raise raise_error(
                ErrorCodes.ORDER_NOT_FOUND,
                "Order not found."
            )
        return order