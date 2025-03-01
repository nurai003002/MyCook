from django.db import models
from ckeditor.fields import RichTextField

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
        
class RecipeCategory(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название категория',
        blank=True, null=True
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Категория (рецепты)'
        verbose_name_plural = 'Категории (рецепты)'
    
class Recipe(models.Model):
    category = models.ForeignKey(
        RecipeCategory, on_delete=models.CASCADE,
        related_name='recipe_category',
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='recipe/',
        verbose_name='Фото рецепта'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    description = RichTextField(
        verbose_name='Описание',
        blank=True, null=True
    )
    video_url = models.URLField(
        verbose_name='Видео рецепта',
        blank=True, null=True
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = 'Рецепты'

class Assortment(models.Model):
    image = models.ImageField(
        verbose_name='Изображение', 
        upload_to='assortiment/'
    )
    title = models.CharField(
        max_length=500,
        verbose_name='Заголовок',
        blank=True, null=True
    )
    description = RichTextField(
        verbose_name='Описание',
        blank=True, null=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Ассортимент'
        verbose_name_plural = 'Ассортименты'

