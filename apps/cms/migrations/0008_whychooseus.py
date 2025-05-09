# Generated by Django 5.0.6 on 2025-03-13 09:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_urlwhatsapp_map'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhyChooseUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.CharField(max_length=400, verbose_name='Описание')),
                ('years', models.IntegerField(verbose_name='кол-во стажа')),
                ('sails_mycook', models.IntegerField(verbose_name='кол-во проданных машин')),
                ('client', models.IntegerField(verbose_name='кол-во клиентов')),
                ('reason_1', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Причина 1')),
                ('reason_2', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Причина 1')),
                ('reason_3', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Причина 1')),
            ],
            options={
                'verbose_name': 'Причины выбрать нас',
                'verbose_name_plural': 'Причины выбрать нас',
            },
        ),
    ]
