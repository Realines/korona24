from django.urls import path
from . import views

app_name = 'services'
urlpatterns = [
    path('', views.services, name='services'),
    path('<str:service_url>/<str:article_url>/', views.service_article, name='article'),
    path('<str:service_url>/<str:parrent_url>/<str:article_url>/', views.service_parrent_article, name='parrent'),
    path('<str:service_url>/', views.service, name='service'),
]
