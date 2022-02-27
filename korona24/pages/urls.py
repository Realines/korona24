from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('vrachi-sk-korona/', views.employees, name='employees'),
    path('', views.about, name='about'),
    path('<str:page_title>', views.page, name='page'),
]
