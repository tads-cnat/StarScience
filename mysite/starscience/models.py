from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 150)
    email = models.EmailField(max_length = 256)
    cpf = models.CharField(max_length = 256)
    password = models.CharField(max_length=50)
    is_administrator = models.BooleanField(default = False)

    def __str__(self):
        return '({}) - {}'.format(self.id, self.name)

    # def like(self, article):

    # def save(self, article):

class Article(models.Model):
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 300)
    url = models.URLField(max_length = 300)
    likes = models.IntegerField()

    # Relationships
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '({}) - {}'.format(self.id, self.title)

class SaveArticle(models.Model):
    created_at = models.DateField(auto_now_add = True)

    # Relationships
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

class LikeArticle(models.Model):
    created_at = models.DateField(auto_now_add = True)

    # Relationships
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length = 200)
    created_at = models.DateField(auto_now_add = True)

    # Relationships
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '({}) - {}'.format(self.id)

class KnowledgeArea(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return '({}) - {}'.format(self.id, self.name)

class KnowledgeSubarea(models.Model):
    name = models.CharField(max_length = 200)
    code = models.CharField(max_length = 200)

    # Relationships
    knowledge_area = models.ForeignKey(KnowledgeArea, on_delete=models.CASCADE)

    def __str__(self):
        return '({}) - {}'.format(self.id, self.name)
