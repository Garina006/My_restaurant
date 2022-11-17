from django.urls import path, include
from .views import reservation_list


urlpatterns = [
    path('', reservation_list),

]