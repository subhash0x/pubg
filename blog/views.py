from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .models import Order


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
    context = {'game' : game}
    if request.GET.get('success', None):
        context['paymentSuccess'] = True
    if game.orders.filter(owner=request.user).exists():
        context['user_has_paid'] = True
    return render(request, 'users/payment.html', context)


def gamerule(request):
    return render(request, 'blog/gamerule.html', {'title': 'gamerule'})

def update_order(request):
    order = Order.objects.get(id=request.POST['orderid'])
    order.total_kill = request.POST['kills']
    order.rank = request.POST['rank']
    order.save()
    return redirect('/payment?id=' + str(order.game.id))
