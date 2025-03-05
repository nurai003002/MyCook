from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название сайта'
    )
    logo = models.ImageField(
        default='no_image.jpg',
        upload_to='logo/',
        verbose_name="Логотип",
        blank=True, null=True
    )   
    logo_favicon = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип favicon'
    )
    phone = models.CharField(
        max_length = 255,
        verbose_name = 'Номер телефона'
    )
    email = models.EmailField(
        verbose_name = 'Почта',
        blank=True, null=True
    )
    address = models.CharField(
        max_length=255,
        verbose_name='Адрес'
    )
    schedule = models.CharField(
        max_length=255,
        verbose_name='График работы'
    )
    facebook = models.URLField(
        verbose_name = 'URL facebook',
        blank=True, null=True
    )
    instagram = models.URLField(
        verbose_name = 'URL instagram',
        blank=True, null=True
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'
    
    
class About(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    description = models.CharField(
        max_length=500,
        verbose_name='Описание'
    )
    
    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = 'О нас '

class AboutInline(models.Model):
    about = models.ForeignKey(
        About, on_delete=models.CASCADE,
        related_name='about_inline'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    description = models.CharField(
        max_length=500,
        verbose_name='Описание'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'