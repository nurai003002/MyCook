from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    description = models.CharField(
        max_length=500,
        verbose_name='Описание',
        blank=True, null=True
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
        
class AboutInline(models.Model):
    about = models.ForeignKey(
        About,on_delete=models.CASCADE,
        related_name='about_inline',
        blank=True, null=True
    )
    icon = models.ImageField(
        upload_to='about/',
        verbose_name='Иконка'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    description = models.CharField(
        max_length=600,
        verbose_name='Описание'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
        