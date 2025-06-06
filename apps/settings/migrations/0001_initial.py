# Generated by Django 5.0.6 on 2025-03-05 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название сайта')),
                ('logo', models.ImageField(blank=True, default='no_image.jpg', null=True, upload_to='logo/', verbose_name='Логотип')),
                ('logo_favicon', models.ImageField(upload_to='logo/', verbose_name='Логотип favicon')),
                ('phone', models.CharField(max_length=255, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('schedule', models.CharField(max_length=255, verbose_name='График работы')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='URL facebook')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='URL instagram')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Настройки сайта',
                'verbose_name_plural': 'Настройки сайта',
            },
        ),
    ]
