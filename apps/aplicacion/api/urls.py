from django.urls import path
from .views import cars_api_view,car_api_view


urlpatterns = [
    path('', cars_api_view,name='cars'),
    path('car/<int:pk>/', car_api_view,name='car'),
]
