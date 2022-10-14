from django import forms
from .models import Review

# class 정의
class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        # fields = ['title', 'content', 'grade']
        fields = '__all__'
