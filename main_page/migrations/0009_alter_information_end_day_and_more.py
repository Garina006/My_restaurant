# Generated by Django 4.1.3 on 2022-11-10 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0008_alter_information_email_1_alter_information_email_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='end_day',
            field=models.CharField(blank=True, max_length=20, verbose_name='Працюємо по (день тижня)'),
        ),
        migrations.AlterField(
            model_name='information',
            name='start_day',
            field=models.CharField(blank=True, max_length=20, verbose_name='Працюємо з (день тижня)'),
        ),
    ]