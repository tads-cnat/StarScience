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

""" 
essas são as rotas definidas pelo DefaultRouter().
GET /articles/ - Lista todos os artigos.
POST /articles/ - Cria um novo artigo.
GET /articles/{id}/ - Retorna os detalhes de um artigo específico.
PUT /articles/{id}/ - Atualiza um artigo específico.
PATCH /articles/{id}/ - Atualiza parcialmente um artigo específico.
DELETE /articles/{id}/ - Exclui um artigo específico.
GET /user/ - Lista todos os usuários.
POST /user/ - Cria um novo usuário.
GET /user/{id}/ - Retorna os detalhes de um usuário específico.
PUT /user/{id}/ - Atualiza um usuário específico.
PATCH /user/{id}/ - Atualiza parcialmente um usuário específico.
DELETE /user/{id}/ - Exclui um usuário específico.
GET /category/ - Lista todas as categorias.
POST /category/ - Cria uma nova categoria.
GET /category/{id}/ - Retorna os detalhes de uma categoria específica.
PUT /category/{id}/ - Atualiza uma categoria específica.
PATCH /category/{id}/ - Atualiza parcialmente uma categoria específica.
DELETE /category/{id}/ - Exclui uma categoria específica. 
"""