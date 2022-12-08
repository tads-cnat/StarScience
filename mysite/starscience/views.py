# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from django.shortcuts import render, get_object_or_404
# from django.views import View
# from .models import Tema, Pergunta, Resposta

# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         articles = Article.objects.all()
#         context = {'articles': articles}
#         return render(request, 'starscience/home.html', context)