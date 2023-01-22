from django.urls import path
from .views import ArticleView, CategoryView

urlpatterns = [
    # AS ARTICLE

    path('articles/', ArticleView.article_index, name='article_index'),
    path('articles/search/', ArticleView.article_search, name='article_search'),
    path('articles/create/', ArticleView.article_create, name='article_create'),
    path('articles/<int:id>/', ArticleView.article_show, name='article_show'),
    path('articles/<int:id>/update/', ArticleView.article_update, name='article_update'),
    path('articles/<int:id>/delete/', ArticleView.article_delete, name='article_delete'),

    # AS CATEGORY

    path('categories/', CategoryView.category_index, name='category_index'),
    path('categories/create/', CategoryView.category_create, name='category_create'),
    path('categories/<int:id>/', CategoryView.category_show, name='category_show'),
    path('categories/<int:id>/update/', CategoryView.category_update, name='category_update'),
    path('categories/<int:id>/delete/', CategoryView.category_delete, name='category_delete'),

]