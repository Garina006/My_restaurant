from django.shortcuts import render
from .models import Category, Dish, Presentation, Events, Gallery, Information, Testimonials, Chefs
import random

# Create your views here.
def main_view(request):

    dishes = Dish.objects.filter(is_visible=True)
    categories = Category.objects.filter(is_visible=True)
    specials = Dish.objects.filter(is_visible=True, is_special=True)
    about = Presentation.objects.filter(is_visible=True, about=True)
    why_us = Presentation.objects.filter(is_visible=True, why_us=True)
    events = Events.objects.filter(is_visible=True)
    photos = Gallery.objects.all().order_by('?')
    greetings = Presentation.objects.filter(is_visible=True, greetings=True)
    chefs = Chefs.objects.filter(is_visible=True)


    return render(request, 'base.html', context={
        'dishes': dishes,
        'categories': categories,
        'specials': specials,
        'about': about,
        'why_us': why_us,
        'events': events,
        'photos': photos,
        'greetings': greetings,
        'chefs': chefs,

    })
