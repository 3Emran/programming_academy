
# Create your models here.
from django.db import models

class Question(models.Model):
    DIFFICULTY = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )

    question_text = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY)
    topic = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    options = models.JSONField()  # {"A": "...", "B": "...", "C": "...", "D": "..."}

    def __str__(self):
        return self.question_text
