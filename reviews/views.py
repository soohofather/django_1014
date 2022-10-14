from contextlib import redirect_stderr
from urllib.request import Request
from django.shortcuts import render, redirect
from .models import Review
from reviews.forms import ReviewForm

# Create your views here.

def index(request):
    reviews = Review.objects.order_by('-pk')

    context = {
        'reviews': reviews
    }
    return render(request, 'reviews/index.html', context)

def create(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect('reviews:index')
    else:
        review_form = ReviewForm()
    
    context = {
        'review_form': review_form
    }

    return render(request, 'reviews/new.html', context)