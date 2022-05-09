from django.urls import path
from . import views

app_name = 'comments'
urlpatterns = [
    path('', views.comments, name='comments'),
    path('send-comment/', views.comments_handler, name='send_comment')
]
