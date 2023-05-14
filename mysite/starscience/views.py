from .models import Article
from .serializers import ArticleSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ArticleViews(APIView):
    def get(self, request, format=None):
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
            serializer = ArticleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    class ArticleDetail(APIView):
        def get_object(self, pk):
            try:
                return Article.objects.get(pk=pk)
            except Article.DoesNotExist:
                raise Http404

        def get(self, request, pk, format=None):
            article = self.get_object(pk)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)

        def put(self, request, pk, format=None):
            article = self.get_object(pk)
            serializer = ArticleSerializer(article, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk, format=None):
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

""" class CategoryView:
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

    def category_update(request, id):
        obj = Category.objects.get(id=id)
        if request.method == 'POST':
            obj.name = request.POST.get('name')
            obj.save()
            return redirect('category_index')
        else:
            return render(request, 'categories/update.html', {'object': obj}) """