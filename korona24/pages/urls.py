from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.about, name='about'),
    path('<str:page_title>', views.page, name='page'),
     
]
