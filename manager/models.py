from django.db import models
from django.core.validators import RegexValidator, EmailValidator
import datetime

# Create your models here.
class UserReservation(models.Model):
    mobile_phone_re = RegexValidator(regex=r'^[+]?380\d{2}([ -])?\d{7}$', message='Невірний формат номеру телефону')
    name = models.CharField("Ваше ім'я", max_length=50, blank=True, null=True)
    persons = models.PositiveSmallIntegerField('Кількість людей', blank=True, null=True)
    phone = models.CharField('Ваш телефон', max_length=15, validators=[mobile_phone_re], blank=True, null=True)
    message = models.TextField('Залиште повідомлення', max_length=500, default='')
    email = models.CharField('Ваш імейл', max_length=50, validators=[EmailValidator(message='Введіть вірний e-mail')],
                             default='')
    date_reserve = models.DateField('Оберіть дату', default=datetime.date.today())
    time_reserve = models.TimeField('Оберіть час', blank=True, null=True)

    is_processed = models.BooleanField(default=False)
    date_in = models.DateTimeField(auto_now_add=True)
    date_modify = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_in',)

    def __str__(self):
        return f"{self.name}: {self.phone}: {self.message[:20]}"


class UserContact(models.Model):

    name = models.CharField("Ваше ім'я", max_length=50, blank=True, null=True)
    email = models.CharField('Ваш імейл', max_length=50, validators=[EmailValidator(message='Введіть вірний e-mail')],
                             default='')
    subject = models.CharField("Тема повідомлення", max_length=50, default='Testimonial')
    message = models.TextField('Залиште повідомлення', max_length=500, default='')

    is_processed = models.BooleanField(default=False)
    date_in = models.DateTimeField(auto_now_add=True)
    date_modify = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_in',)

    def __str__(self):
        return f"{self.name}: {self.subject}"
