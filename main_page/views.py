from django.shortcuts import render, redirect
from .models import Category, Dish, Presentation, Events, Gallery, Information, Testimonials, Chefs
from .forms import UserReservationForm
import random

# Create your views here.
def main_view(request):

    form_reserve = UserReservationForm(request.POST or None)

    if form_reserve.is_valid():
        form_reserve.save()
        return redirect('/')


    dishes = Dish.objects.filter(is_visible=True)
    categories = Category.objects.filter(is_visible=True)
    specials = Dish.objects.filter(is_visible=True, is_special=True)
    about = Presentation.objects.filter(is_visible=True, about=True)
    why_us = Presentation.objects.filter(is_visible=True, why_us=True)
    events = Events.objects.filter(is_visible=True)
    photos = Gallery.objects.all()
    photos = random.sample(list(photos), 8)
    greetings = Presentation.objects.filter(is_visible=True, greetings=True)
    chefs = Chefs.objects.filter(is_visible=True)
    testimonials = Testimonials.objects.filter(is_visible=True)
    info = Information.objects.all()


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
        'testimonials': testimonials,
        'info': info,
        'form_reserve': form_reserve,

    })
