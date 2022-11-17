from django.urls import path, include
from .views import reservation_list, reservation_close, message_list, message_processed

app_name = 'manager'

urlpatterns = [
    path('', reservation_list, name='reservation_list'),
    path('message/', message_list, name='message_list'),
    path('update/<int:pk>/', reservation_close, name='reservation_close'),
    path('message/update/<int:pk>/', message_processed, name='message_processed'),


]