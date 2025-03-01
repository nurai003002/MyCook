from django.db import models

# Create your models here.

class RecipeBanner(models.Model):
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Фото для баннера'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Баннер (Рецепты)'
        verbose_name_plural = 'Баннер (Рецепты)'