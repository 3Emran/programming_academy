from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
    
    options = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        help_text='Enter options as JSON: {"A": "Option A", "B": "Option B"}'
    )
