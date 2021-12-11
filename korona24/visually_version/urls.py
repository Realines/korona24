from django.urls import path
from . import views

app_name = 'visually_version'
urlpatterns = [
    path('<int:visually_version>/', views.set_visually_version, name='set_version')
]
