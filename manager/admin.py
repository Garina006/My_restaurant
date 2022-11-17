from django.contrib import admin
from .models import UserReservation, UserContact

# Register your models here.
admin.site.register(UserReservation)
admin.site.register(UserContact)
