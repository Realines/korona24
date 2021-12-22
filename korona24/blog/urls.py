from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.articles, name='articles'),
    path('<int:article_id>/', views.article, name='article'),
    path('pagination/', views.pagination_articles, name='pagination-articles'),
]
