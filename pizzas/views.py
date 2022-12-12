from django.shortcuts import render, redirect
from .models import *
'''from .comments import *'''

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

def pizza_options(request):
    pizza_options = Pizza.objects.order_by('pizza_name')

    context = {'all_pizzas':pizza_options}

    return render(request, 'pizzas/pizza_options.html', context)


def pizza_option(request, pizza_id):
    p = Pizza.objects.get(id=pizza_id)

    t = Topping.objects.filter(pizza=p)
    
    context = {'pizza':p, 'toppings':t}

    return render(request, 'pizzas/pizza_option.html', context)


'''
def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    
    if request.method != 'POST':
        comment = PizzaComment()
    else:
        print(request.POST)
        comment = PizzaComment(data=request.POST)
        if comment.is_valid():
            new_comment = comment.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()
            return redirect('MainApp:topic', pizza_id=pizza_id)
     
    context = {'comment':comment, 'pizza':pizza}
    return render(request, 'MainApp/new_entry.html', context)'''