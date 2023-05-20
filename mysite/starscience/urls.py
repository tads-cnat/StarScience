from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet ,CategoryViewSet ,UserViewSet

router = DefaultRouter()
router.register('articles', ArticleViewSet)
router.register('user', UserViewSet)
router.register('category',CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]