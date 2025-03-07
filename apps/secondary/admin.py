from django.contrib import admin

from apps.secondary import models
# Register your models here.

class AboutInlineTabularInline(admin.TabularInline):
    model = models.AboutInline
    extra = 1

class WhyTheyChooseUsInlineTabular(admin.TabularInline):
    model = models.WhyTheyChooseUsInline
    extra = 1
    
@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_filter = ('id', 'title')
    inlines = (AboutInlineTabularInline, )
    
@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')
    
@admin.register(models.RecipeCategory)
class RecipeCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')
    
@admin.register(models.Guarantee)
class GuaranteeAdmin(admin.ModelAdmin):
    list_display = ('id', 'delivery_title')
    list_filter = ('id', 'delivery_title')
    
@admin.register(models.Assortment)
class AssortmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')

@admin.register(models.OwnMyCookCategory)
class OwnMyCookCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')

@admin.register(models.OwnMyCook)
class OwnMyCookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')
    
@admin.register(models.WhyTheyChooseUs)
class WhyTheyChooseUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')
    inlines = (WhyTheyChooseUsInlineTabular, )