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
    image = models.ImageField(
        upload_to='guarentee',
        verbose_name='Фотография',
        blank=True, null=True
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
        
class Guarantee(models.Model):
    delivery_title = models.CharField(
        max_length=255,
        verbose_name='Заголовок доставки',
        blank=True, null=True
    )
    description_delivery = RichTextField(
        verbose_name='Информация об доставке',
        blank=True, null=True
    )
    delivery_image = models.ImageField(
        upload_to='guarentee',
        verbose_name='Фотография (доставке)',
        blank=True, null=True
    )
    guarantee = models.CharField(
        max_length=255,
        verbose_name='Заголовок горантии',
        blank=True, null=True
    )
    guarantee_description = RichTextField(
        verbose_name='Информация об горантии',
        blank=True, null=True
    )
    guarantee_image = models.ImageField(
        upload_to='guarentee',
        verbose_name='Фотография (горантии)',
        blank=True, null=True
    )
    props = models.CharField(
        max_length=255,
        verbose_name='Информация об реквизитах',
        blank=True, null=True
    )
    props_description = RichTextField(
        verbose_name='Информация об реквизитах',
        blank=True, null=True
    )
    props_image = models.ImageField(
        upload_to='guarentee',
        verbose_name='Фотография (реквизиты)',
        blank=True, null=True
    )
    def __str__(self):
        return self.delivery_title
    
    class Meta:
        verbose_name = 'Гарантия'
        verbose_name_plural = 'Гарантии'
        
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
        
class OwnMyCookCategory(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок' 
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Сам mycook категория'
        verbose_name_plural = 'Сам mycook категория'
        
class OwnMyCook(models.Model):
    category = models.ForeignKey(
        OwnMyCookCategory, on_delete=models.CASCADE,
        related_name='own_title'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок' 
    )
    description = models.CharField(
        max_length=600,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Фотграфия'
    )
    advantage_1 = models.CharField(
        max_length=255,
        verbose_name='преимущество 1' 
    )
    advantage_2 = models.CharField(
        max_length=255,
        verbose_name='преимущество 2' 
    )
    advantage_3 = models.CharField(
        max_length=255,
        verbose_name='преимущество 3' 
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Сам mycook'
    
class WhyTheyChooseUs(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    description = models.CharField(
        max_length=700,
        verbose_name='Описание'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Почему выбирают нас?'
        verbose_name_plural = 'Почему выбирают нас?'

class WhyTheyChooseUsInline(models.Model):
    reason = models.ForeignKey(
        WhyTheyChooseUs, on_delete=models.CASCADE,
        related_name='reason_inline'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    description = models.CharField(
        max_length=700,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='why/',
        verbose_name='Фотография'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Почему выбирают нас?'
        verbose_name_plural = 'Почему выбирают нас?'