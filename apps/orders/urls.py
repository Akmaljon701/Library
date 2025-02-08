from django.urls import path
from apps.orders import views

urlpatterns = [
    path('create/', views.create_order, name='create_order'),
    path('<int:pk>/update/', views.update_order, name='update_order'),
    path('', views.get_orders, name='get_orders'),
    path('user-orders', views.get_user_orders, name='get_user_orders'),
    path('user-orders/<int:pk>', views.get_user_order, name='get_user_order'),
]
