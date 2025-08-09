from django.shortcuts import render
from .models import Question
from .utils import generate_adaptive_quiz  # if you're using adaptive logic

def start_quiz(request):
    all_questions = Question.objects.all()
    if not all_questions.exists():
        return render(request, 'quiz/start_quiz.html', {'questions': []})

    selected_questions = generate_adaptive_quiz(all_questions, target_difficulty=10)

    return render(request, 'quiz/start_quiz.html', {
        'questions': selected_questions
    })
