from django.db import models
from ckeditor.fields import RichTextField
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
        
class Faqs(models.Model):
    main_title = models.CharField(
        max_length=255,
        verbose_name='Главный заголовок'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    
    def __str__(self):
        return self.main_title
    
    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
        
class FAQsInline(models.Model):
    faqs = models.ForeignKey(
        Faqs, on_delete=models.CASCADE,
        related_name='faqs_inline'
    )
    question = models.CharField(
        max_length=255,
        verbose_name='Вопрос'
    )
    answer = models.CharField(
        max_length=255,
        verbose_name='Ответ'
    )
    
    def __str__(self):
        return f"{self.question} - {self.answer}"
    
    class Meta:
        verbose_name = 'Часто задаваемые вопрос'
        verbose_name_plural = 'Часто задаваемые вопросы'
        
class ProductBanner(models.Model):
    image = models.ImageField(
        upload_to='main_image',
        verbose_name='Фото'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    description = RichTextField(
        verbose_name='Описание',
        blank=True, null=True
    )
    button_1 = models.CharField(
        max_length=255,
        verbose_name='Название для кнопки'
    )
    button_1_url = models.CharField(
        max_length=255,
        verbose_name='URL для кнопки'
    )
    button_2 = models.CharField(
        max_length=255,
        verbose_name='Название для кнопки'
    )
    button_2_url = models.CharField(
        max_length=255,
        verbose_name='URL для кнопки'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Главный баннер'
        verbose_name_plural = 'Главный баннер'

class Review(models.Model):
    text = models.CharField(
        max_length=600,
        verbose_name='Отзыв',
        blank=True, null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        blank=True, null=True
    )
    
    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        
class UrlWhatsapp(models.Model):
    url = models.URLField(
        verbose_name='URL для вотс (доставка)'
    )
    map = models.URLField(
        verbose_name='URL для контакт (карта)'
    )
    
    class Meta:
        verbose_name = "Ссылка для кнопки доставка"
        verbose_name_plural = 'Ссылка для кнопки доставка'