from django.urls import path
from . import views

app_name = 'starscience'
urlpatterns = [
    path('', views.index, name='home'),
    path('article/<int:pk>/', views.ArticleViews.detailArticle, name='detail_article'),
    path(
        'article/adicionar',
        views.ArticleViews.saveArticle, name='add_article'
    ),
    path(
        'article/<int:pk>/atualizar',
        views.ArticleViews.updateArticle, name='update_article'
    ),
    path(
        'article/<int:pk>/deletar',
        views.ArticleViews.deleteArticle, name='delete_article'
    ),
    path(
        'article/form',
        views.ArticleViews.formArticle, name='form_article'
    ),

]
