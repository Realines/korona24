from django.urls import path
from . import views

app_name = 'visual_version_handler'
urlpatterns = [
    path('<int:visual_version>/', views.set_visual_version, name='set_version')
]
