from django.urls import path
from . import views

app_name = 'services'
urlpatterns = [
    path('', views.services, name='services'),
    path('<int:service_id>/', views.service, name='service'),
    path('prices/', views.prices, name='prices'),
]
