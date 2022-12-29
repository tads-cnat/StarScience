from django.shortcuts import redirect, render
from .models import *

def index(request):
    return render(request, 'index.html')

class ArticleViews:
     def listArticle(request):
        article_lists = Article.objects.all()
        context = {'article_lists': article_lists}
        return render(request, 'article/listArticle.html', context)

    def formArticle(request):
        return render(request, 'article/formArticle.html')

    def saveArticle(request):
        c = Article(title=request.POST['title'],
                   description=request.POST['description'],
                   url=request.POST['url'],
                   likes=request.POST['likes'])
        c.save()

        return redirect('/listArticle')

    def deleteArticle(request, id):
        c = Article.objects.get(pk=id)
        c.delete()
        return redirect('/listArticle')

    def detailArticle(request, id):
        article = Article.objects.get(pk=id)
        return render(request, 'article/formEditArticle.html', {'article': article} )

    def updateArticle(request, id):
        c = Article.objects.get(pk=id)
        c.title = request.POST['title']
        c.description = request.POST['description']
        c.url = request.POST['url']
        c.likes = request.POST['likes']
        c.save()

        return redirect('/listArticle')