from django.shortcuts import render, redirect
from .models import UserReservation, UserContact
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.
def is_manager(user):
    return user.groups.filter(name='manager').exists()


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def reservation_list(request):
    reservations = UserReservation.objects.filter(is_processed=False)
    return render(request, 'reserve_list.html', context={'reserve_list': reservations})


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def reservation_close(request, pk):
    UserReservation.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:reservation_list')


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def message_list(request):
    messages = UserContact.objects.filter(is_processed=False)
    return render(request, 'message_list.html', context={'message_list': messages})


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def message_processed(request, pk):
    UserContact.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:message_list')

