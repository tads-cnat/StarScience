from django.urls import path
from . import views

app_name = 'starscience'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('tema/<int:pk>/', views.TemaView.as_view(), name='tema'),
    path(
        'tema/adicionar',
        views.NovoTemaView.as_view(), name='add_tema'
    ),
    path(
        'tema/<int:pk>/perguntar',
        views.NovaPerguntaView.as_view(), name='add_perg'
    ),
    path(
        'pergunta/<int:pk>/responder',
        views.AdicionaRespostaView.as_view(), name='add_resp'
    ),
    path(
        'resposta/<int:pk>/votar',
        views.VotarEmRespostaView.as_view(), name='vota_resp'
    ),
]
