from django.urls import path
from . import views

app_name = 'employees'
urlpatterns = [
    path('<int:employee_id>/', views.employee, name='service'),
]
