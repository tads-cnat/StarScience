from rest_framework import serializers
from .models import Article, User, Category

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'cpf', 'password', 'is_administrator')


class ArticleSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Article
        fields = ('id', 'title', 'description', 'url', 'likes', 'created_at', 'user', 'user_name', 'category', 'category_name')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
