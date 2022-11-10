from django.contrib import admin
from .models import Category, Dish, Events, Presentation, Gallery, Information, Testimonials, Chefs

# Register your models here.
admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Events)
admin.site.register(Presentation)
admin.site.register(Gallery)
admin.site.register(Information)
admin.site.register(Testimonials)
admin.site.register(Chefs)


