# Generated by Django 5.0.6 on 2025-03-04 10:02

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0007_aboutinline_image_guarantee_delivery_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='guarantee',
            name='description_delivery',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Информация об доставке'),
        ),
        migrations.AddField(
            model_name='guarantee',
            name='guarantee_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Информация об горантии'),
        ),
        migrations.AddField(
            model_name='guarantee',
            name='props_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Информация об реквизитах'),
        ),
        migrations.AlterField(
            model_name='guarantee',
            name='delivery_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок доставки'),
        ),
        migrations.AlterField(
            model_name='guarantee',
            name='guarantee',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок горантии'),
        ),
        migrations.AlterField(
            model_name='guarantee',
            name='props',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Информация об реквизитах'),
        ),
    ]
