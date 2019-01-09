from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required


def home(request):
    context = {
        'posts': Post.objects.all().order_by('-date_posted')
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

@login_required
def payment(request):
    return render(request, 'users/payment.html')
