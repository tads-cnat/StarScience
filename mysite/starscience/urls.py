from django.urls import path
from .views import article_index, article_create, article_show, article_update, article_delete

urlpatterns = [
    # AS ARTICLE
    path('articles/', article_index, name='article_index'),
    path('articles/create/', article_create, name='article_create'),
    path('articles/<int:id>/', article_show, name='article_show'),
    path('articles/<int:id>/update/', article_update, name='article_update'),
    path('articles/<int:id>/delete/', article_delete, name='article_delete'),

    # # AS CATEGORY
]