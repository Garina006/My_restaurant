from django.db import models
import uuid
import os


class Category(models.Model):
    title = models.CharField('Назва категорії', max_length=50, unique=True, db_index=True)
    is_visible = models.BooleanField('Відображати', default=True)
    position = models.PositiveSmallIntegerField('Позиція', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорія меню'
        verbose_name_plural = 'Категорії меню'
        ordering = ['position']


class Dish(models.Model):

    def get_file_name(self, file_name: str):
        ext = file_name.strip().split()[-1]
        f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/dishes', f'{uuid.uuid4()}.{ext}')

    title = models.CharField('Назва страви', max_length=50, unique=True, db_index=True)
    ingredients = models.CharField('Інгредієнти', max_length=100)
    price = models.DecimalField('Ціна', max_digits=8, decimal_places=2)
    is_special = models.BooleanField('Спеціальна пропозиція', default=False)
    is_visible = models.BooleanField('Відображати', default=True)
    position = models.PositiveSmallIntegerField('Позиція')
    desc = models.TextField('Опис страви', max_length=500, blank=True)
    photo = models.ImageField('Завантажити фото', upload_to=get_file_name)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страва'
        verbose_name_plural = 'Страви'
        ordering = ['category', 'position']


class Presentation(models.Model):

    def get_file_name(self, file_name: str):
        ext = file_name.strip().split()[-1]
        f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/presentation', f'{uuid.uuid4()}.{ext}')

    title = models.CharField('Назва презентації', max_length=50, unique=True, db_index=True)
    desc = models.TextField('Опис', max_length=500, blank=True)
    photo = models.ImageField('Завантажити фото', upload_to=get_file_name, blank=True)
    video = models.URLField('Завантажити відео', blank=True)
    is_visible = models.BooleanField('Відображати', default=True)
    why_us = models.BooleanField('Розділ "Чому ми"', default=True)
    about = models.BooleanField('Розділ "Про нас"', default=False)
    greetings = models.BooleanField('Розділ "Вітання від ресторану"', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Презентація'
        verbose_name_plural = 'Презентації'


class Gallery(models.Model):

    def get_file_name(self, file_name: str):
        ext = file_name.strip().split()[-1]
        f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/gallery', f'{uuid.uuid4()}.{ext}')

    photo = models.ImageField('Завантажити фото', upload_to=get_file_name)


    class Meta:
        verbose_name = 'Галерея фото'
        verbose_name_plural = 'Галерея фото'


class Events(models.Model):

    def get_file_name(self, file_name: str):
        ext = file_name.strip().split()[-1]
        f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/events', f'{uuid.uuid4()}.{ext}')

    title = models.CharField('Назва події', max_length=50, unique=True, db_index=True)
    desc = models.TextField('Опис події', max_length=500, blank=True)
    price = models.DecimalField('Вартість', max_digits=8, decimal_places=2)
    photo = models.ImageField('Завантажити фото', upload_to=get_file_name)
    is_visible = models.BooleanField('Відображати', default=True)
    date = models.DateTimeField('Дата та час події', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подія'
        verbose_name_plural = 'Події'


class Chefs(models.Model):

    def get_file_name(self, file_name: str):
        ext = file_name.strip().split()[-1]
        f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/chefs', f'{uuid.uuid4()}.{ext}')

    name = models.CharField("Ім'я", max_length=20, db_index=True)
    surname = models.CharField("Призвище", max_length=20)
    job_title = models.CharField("Посада", max_length=20)
    photo = models.ImageField('Завантажити фото', upload_to=get_file_name)
    is_visible = models.BooleanField('Відображати', default=True)

    def __str__(self):
        return f'{self.job_title} {self.surname} {self.name[0]}.'

    class Meta:
        verbose_name = 'Кухар'
        verbose_name_plural = 'Кухарі'


class Testimonials(models.Model):

    def get_file_name(self, file_name: str):
        ext = file_name.strip().split()[-1]
        f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/testimonials', f'{uuid.uuid4()}.{ext}')

    name = models.CharField("Ім'я", max_length=20, db_index=True)
    surname = models.CharField("Призвище", max_length=20)
    profession = models.CharField("Професія", max_length=30)
    photo = models.ImageField('Завантажити фото', upload_to=get_file_name)
    text = models.TextField('Відгук', max_length=500, blank=True)
    is_visible = models.BooleanField('Відображати', default=True)

    class Meta:
        verbose_name = 'Відгук'
        verbose_name_plural = 'Відгуки'


class Information(models.Model):
    street = models.CharField('Вулиця та будинок', max_length=20, db_index=True)
    city = models.CharField('Місто', max_length=20)
    start_day = models.CharField('Працюємо з (день тижня)', max_length=20, blank=True)
    end_day = models.CharField('Працюємо по (день тижня)', max_length=20, blank=True)
    start_time = models.TimeField('Відкриваємось о (час)', blank=True)
    close_time = models.TimeField('Закриваємось о (час)', blank=True)
    email_1 = models.EmailField('Імейл_1', default='')
    email_2 = models.EmailField('Імейл_2', blank=True, default='')
    phone_1 = models.CharField('Телефон_1', max_length=13, default='')
    phone_2 = models.CharField('Телефон_2', max_length=13, blank=True, default='')

    class Meta:
        verbose_name = 'Інформація про ресторан'
        verbose_name_plural = 'Інформація про ресторан'

