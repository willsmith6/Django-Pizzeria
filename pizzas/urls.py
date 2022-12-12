from django.urls import path
from . import views


app_name = 'pizzas'

urlpatterns = [
    path('',views.index,name='index'),
    path('pizza_options',views.pizza_options,name='pizza_options'),
    path('pizza_options/<int:pizza_id>/',views.pizza_option,name='pizza_option'),
]

