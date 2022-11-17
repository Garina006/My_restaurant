from django import forms
from manager.models import UserReservation, UserContact


class UserReservationForm(forms.ModelForm):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={
                            'type': "text",
                            'name': "name",
                            'class': "form-control",
                            'id':  "name",
                            'placeholder':  "Ваше ім'я",
                            'data - rule':  "minlen:4",
                            'data - msg':  "Please enter at least 4 chars",
                            }))

    persons = forms.IntegerField(widget=forms.NumberInput(attrs={
                            'type': 'number',
                            'class': 'form-control',
                            'name': 'people',
                            'id': 'people',
                            'placeholder': 'Кількість гостей',
                            'data - rule': 'minlen:1',
                            'data - msg': 'Введіть щонайменше 1 символ',
                             }))

    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
                            'type': 'text',
                            'class': 'form-control',
                            'name': 'phone',
                            'id': 'phone',
                            'placeholder': 'Ваш телефон',
                            'data-rule': 'minlen:10',
                            'data-msg': 'Введіть щонайменше 10 символів',
                            }))

    message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
                            'class': 'form-control',
                            'name': 'message',
                            'rows': '5',
                            'placeholder': 'Повідомлення',
                            }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
                            'type': 'email',
                            'class': 'form-control',
                            'name': 'email',
                            'id': 'email',
                            'placeholder': 'Ваш Імейл',
                            'data-rule': 'email',
                            'data-msg': 'Будь ласка, введіть вірний імейл',
                            }))

    date_reserve = forms.DateField(widget=forms.DateInput(attrs={
                            'type': 'text',
                            'name': 'date',
                            'class': 'form-control',
                            'id': 'date',
                            'placeholder': 'Оберіть дату',
                            'data-rule': 'minlen:4',
                            'data-msg': 'Введіть щонайменше 4 символи',
                            }))

    time_reserve = forms.TimeField(widget=forms.TimeInput(attrs={
                            'type': 'text',
                            'class': 'form-control',
                            'name': 'time',
                            'id': 'time',
                            'placeholder': 'Оберіть час',
                            'data-rule': 'minlen:4',
                            'data-msg': 'Введіть щонайменше 4 символи',
                            }))

    class Meta:
        model = UserReservation
        fields = ('name', 'persons', 'phone', 'message', 'email', 'date_reserve', 'time_reserve')


class UserContactForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
                            'type': 'text',
                            'name': 'name',
                            'class': 'form-control',
                            'id': 'name',
                            'placeholder': "Введіть ваше ім'я",
                            'required': '',
                            }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                            'type': 'email',
                            'class': 'form-control',
                            'name': 'email',
                            'id': 'email',
                            'placeholder': 'Введіть ваш імейл',
                            'required': '',
                            }))
    subject = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
                            'type': 'text',
                            'class': 'form-control',
                            'name': 'subject',
                            'id': 'subject',
                            'placeholder': 'Тема повідомлення',
                            'required': '',
                            }))
    message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
                            'class': 'form-control',
                            'name': 'message',
                            'rows': '5',
                            'placeholder': 'Введіть ваше повідомлення',
                            'required': '',
                            }))

    class Meta:
        model = UserContact
        fields = ('name', 'email', 'subject', 'message')
