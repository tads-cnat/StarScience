from django.urls import path
from .views import ArticleView

urlpatterns = [
    # AS ARTICLE

    path('articles/', ArticleView.article_index, name='article_index'),
    path('articles/create/', ArticleView.article_create, name='article_create'),
    path('articles/<int:id>/', ArticleView.article_show, name='article_show'),
    path('articles/<int:id>/update/', ArticleView.article_update, name='article_update'),
    path('articles/<int:id>/delete/', ArticleView.article_delete, name='article_delete'),
]