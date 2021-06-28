from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):

    if request.method == "POST":
        fd = request.POST.get('food_consumed', '')
        consumed = Food.objects.get(id=fd)
        user = request.user
        consume = Consume(user=user, food_consume=consumed)
        consume.save()
        foods = Food.objects.all()
        consumed_food = Consume.objects.filter(user=request.user)
    else:
        foods = Food.objects.all()
        consumed_food = Consume.objects.filter(user=request.user)

    return render(request, 'app/index.html', {'foods':foods, 'consumed_food':consumed_food})

def delete_consume(request, id):
    consume_food = Consume.objects.get(id=id)
    if request.method == "POST":
        consume_food.delete()
        return redirect('/')

    return render(request, 'app/delete.html')

