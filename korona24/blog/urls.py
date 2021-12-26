from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.articles, name='articles'),
    path('<str:article_url>/', views.article, name='article'),
    path('pagination/', views.pagination_articles, name='pagination-articles'),
]
