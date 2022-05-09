from django.urls import path
from . import views

app_name = 'employees'
urlpatterns = [
    path('<str:employee_url>/', views.employee, name='employee'),
]
