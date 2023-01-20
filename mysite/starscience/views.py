from django.shortcuts import render, redirect
from .models import Article

class ArticleView:
    def article_index(request):
        objects = Article.objects.all()
        return render(request, 'articles/index.html', {'objects': objects})

    def article_create(request):
        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            url = request.POST.get('url')
            likes = request.POST.get('likes')

            Article.objects.create(title=title, description=description, url=url, likes=likes)
            return redirect('article_index')
        else:
            return render(request, 'articles/create.html')

    def article_show(request, id):
        obj = Article.objects.get(id=id)
        return render(request, 'articles/show.html', {'object': obj})

    def article_update(request, id):
        obj = Article.objects.get(id=id)
        if request.method == 'POST':
            obj.title = request.POST.get('title')
            obj.description = request.POST.get('description')
            obj.url = request.POST.get('url')
            obj.likes = request.POST.get('likes')
            obj.save()
            return redirect('article_index')
        else:
            return render(request, 'articles/update.html', {'object': obj})

    def article_delete(request, id):
        obj = Article.objects.get(id=id)
        if request.method == 'POST':
            obj.delete()
            return redirect('article_index')
        else:
            return render(request, 'articles/delete.html', {'object': obj})