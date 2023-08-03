import requests
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Article, Category, User, SaveArticle
from .serializers import ArticleSerializer, CategorySerializer, UserSerializer, SaveArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SaveArticleViewSet(viewsets.ModelViewSet):
    queryset = SaveArticle.objects.all()
    serializer_class = SaveArticleSerializer

# In your Django view or middleware
from django.http import HttpResponse

def my_view(request):
    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = 'http://localhost:5173'
    response['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'  # Add any other allowed HTTP methods here
    response['Access-Control-Allow-Headers'] = 'Content-Type'  # Add any other allowed headers here
    return response

# Definindo acesso a Elsevier Scopus Search.
class ArticleSearchViewSet(viewsets.ViewSet):
    api_key = "145da3db818e55af26df2fb05bd0db81"

    def list(self, request):
        query = request.GET.get('query', '')

        url = "https://api.elsevier.com/content/search/scopus"
        params = {
            "query": query,
            "apiKey": self.api_key
            
            
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            articles = data["search-results"]["entry"]
            results = []
            for article in articles:
                title = article["dc:title"]
                authors = article["dc:creator"]
                doi = article["prism:doi"]
                year = article.get("prism:coverDate")
                
                results.append({
                    "title": title,
                    "authors": authors,
                    "year": year,
                    "doi": doi
                    
                    
                })

            return Response(results)
        else:
            return Response({"error": "Failed to fetch articles"}, status=response.status_code)