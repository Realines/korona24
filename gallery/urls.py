from django.urls import path
from . import views

app_name = 'gallery'
urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('pagination/', views.pagination_gallery, name='pagination'),
]
