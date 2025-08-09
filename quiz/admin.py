# quiz/admin.py

from django.contrib import admin
from .models import Question
from .forms import QuestionForm

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'difficulty', 'topic')
    list_filter = ('difficulty', 'topic')
    search_fields = ('question_text', 'topic')
    form = QuestionForm
    list_display = ('question_text', 'difficulty', 'topic')
