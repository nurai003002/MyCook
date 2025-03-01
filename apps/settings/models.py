from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.
# class Setting(models.Model):
#     logo = models.ImageField(
#         upload_to='setting/',
#         verbose_name='Лого сайта'
#     ) 
#     title = models.CharField(
#         max_length = 255,
#         verbose_name = 'Название сайта'
#     )
#     phone = models.CharField(
#         max_length = 255,
#         verbose_name = 'Номер телефона'
#     )
#     email = models.EmailField(
#         verbose_name = 'Почта',
#         blank=True, null=True
#     )
#     address = models.CharField(
#         max_length=255,
#         verbose_name='Адрес'
#     )
#     schedule = models.CharField(
#         max_length=255,
#         verbose_name='График работы'
#     )
#     facebook = models.URLField(
#         verbose_name = 'URL facebook',
#         blank=True, null=True
#     )
#     instagram = models.URLField(
#         verbose_name = 'URL instagram',
#         blank=True, null=True
#     )
#     updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title
    
    # def get_absolute_url(self):
    #     return reverse('setting_detail', args=[self.id]) 
    
    # class Meta:
    #     verbose_name = 'Настройки сайта'
    #     verbose_name_plural = 'Настройки сайта'


