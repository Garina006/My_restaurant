# Generated by Django 4.1.3 on 2022-11-10 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0005_alter_information_end_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='email_1',
            field=models.EmailField(max_length=254, verbose_name='Імейл_1'),
        ),
        migrations.AlterField(
            model_name='information',
            name='phone_1',
            field=models.CharField(max_length=13, verbose_name='Телефон_1'),
        ),
    ]