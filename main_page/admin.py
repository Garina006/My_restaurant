from django.contrib import admin
from .models import Category, Dish, Events, Presentation, Gallery

# Register your models here.
admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Events)
admin.site.register(Presentation)
admin.site.register(Gallery)


