from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    content = models.TextField()
    difficulty_score = models.IntegerField()
    topic = models.CharField(max_length=100)
    options = models.JSONField()  # {'a': '...', 'b': '...', ...}
    correct_option = models.CharField(max_length=1)

    def __str__(self):
        return self.content[:50]

class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    generated_at = models.DateTimeField(auto_now_add=True)
    target_difficulty = models.IntegerField()

class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
