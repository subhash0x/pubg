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
    gameId = request.GET['id']
    print(gameId)
    game = Post.objects.get(id=gameId)

    return render(request, 'users/payment.html', {'game' : game})


def gamerule(request):
    return render(request, 'blog/gamerule.html', {'title': 'gamerule'})
