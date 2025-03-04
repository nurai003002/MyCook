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