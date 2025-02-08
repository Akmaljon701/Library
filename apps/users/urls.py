from django.urls import path

from apps.users import views

urlpatterns = [
    path('login', views.LoginAPIView.as_view()),
    path('refresh', views.RefreshTokenAPIView.as_view()),
    path('logout', views.LogoutAPIView.as_view()),
]
