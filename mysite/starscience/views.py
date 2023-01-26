from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Category

class ArticleView:
    def article_index(request):
        objects = Article.objects.all()
        return render(request, 'articles/index.html', {'objects': objects})

    def article_search(request):
        if request.method == 'POST':
            search_query = request.POST['query']
            if search_query:
                search_results = Article.objects.filter(title__contains=search_query)
                return render(request, 'articles/search.html', {'objects': search_results})
            else:
                return redirect('article_index')
        else:
            return redirect('article_index')


    def article_create(request):
        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            url = request.POST.get('url')
            likes = request.POST.get('likes')
            category_name = request.POST.get('category_name')
            category = get_object_or_404(Category, name=category_name)

            Article.objects.create(title=title, description=description, url=url, likes=likes, category=category)
            return redirect('article_index')
        else:
            category_names_list = Category.objects.values_list('name')
            return render(request, 'articles/create.html', {'category_names_list': category_names_list})

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
            obj.category = get_object_or_404(Category, name=request.POST.get('category_name'))
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

class CategoryView:
    def category_index(request):
        objects = Category.objects.all()
        return render(request, 'categories/index.html', {'objects': objects})

    def category_create(request):
        if request.method == 'POST':
            name = request.POST.get('name')

            Category.objects.create(name=name)
            return redirect('category_index')
        else:
            return render(request, 'categories/create.html')

    def category_delete(request, id):
        obj = Category.objects.get(id=id)
        if request.method == 'POST':
            obj.delete()
            return redirect('category_index')
        else:
            return render(request, 'categories/delete.html', {'object': obj})