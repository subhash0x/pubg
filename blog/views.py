from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .models import Order
from django.db.models import Count
from django.contrib import messages


def home(request):
    context = {
        'posts': Post.objects.all().order_by('-date_posted')[:5]
        }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def faq(request):
    return render(request, 'blog/faq.html', {'title': 'FAQ'})

def howtojoin(request):
    return render(request, 'blog/howtojoin.html', {'title': 'how to join'})

def howtoPay(request):
        return render(request, 'blog/howtoPay.html', {'title': 'how to Pay'})

def joininroom(request):
            return render(request, 'blog/joininroom.html', {'title': 'Join Room'})

@login_required
def seo(request):
    return render(request, 'blog/googlefcd4e01ee457c3df.html', {'title': 'seo'})

@login_required
def payment(request):
    if not request.user.profile.pubgusername:
        messages.success(request, f'Please update your profile first')
        return redirect('profile')
    gameId = request.GET['id']
    print(gameId)
    game = Post.objects.get(id=gameId)
    context = {'game' : game }
    success = request.GET.get('success', None)

    if success is not None:
        print(success)
        if success == 'true':
            context['paymentSuccess'] = True
        else:
            context['paymentFailed'] = True
    if game.orders.filter(owner=request.user, payment_status='TXN_SUCCESS').exists():
        context['user_has_paid'] = True
    return render(request, 'users/payment.html', context)


#
# def wow(request):
#     x = game.orders.filter(payment_status='TXN_SUCCESS').count()
#     context['x'] = True
#     print(x)
#     return render(request, 'users/home.html', x)

def gamerule(request):
    return render(request, 'blog/gamerule.html', {'title': 'gamerule'})

@login_required
def update_order(request):
    order = Order.objects.get(id=request.POST['orderid'])
    order.total_kill = request.POST['kills']
    order.rank = request.POST['rank']
    order.prize_amount = request.POST['prize_amount']
    order.save()
    return redirect('/payment?id=' + str(order.game.id))

@login_required
def roominfo(request):
    post = Post.objects.get(id=request.POST['gameid'])
    post.room_id = request.POST['room_id']
    post.room_pass = request.POST['room_pass']
    post.save()
    return redirect('/payment?id=' + str(post.id))
