from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Dish, Events, Presentation, Gallery, Information, Testimonials, Chefs

class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('desc')


# Register your models here.
admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Events, NewsAdmin)
admin.site.register(Presentation, NewsAdmin)
admin.site.register(Gallery)
admin.site.register(Information)
admin.site.register(Testimonials)
admin.site.register(Chefs)


