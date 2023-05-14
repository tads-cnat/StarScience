from django.urls import path
from .views import ArticleViews


urlpatterns = [
    # AS ARTICLE

    path('articles/', ArticleViews.as_view()),
    path('articles/<int:pk>/', ArticleViews.as_view()),

]