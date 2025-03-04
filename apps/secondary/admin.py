from django.contrib import admin
from apps.secondary.models import About, AboutInline, Recipe, RecipeCategory, Guarantee, Assortment, Details, DetailsInline
# Register your models here.

class AboutInlineTabularInline(admin.TabularInline):
    model = AboutInline
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_filter = ('id', 'title')
    inlines = (AboutInlineTabularInline, )

    
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')
    
@admin.register(RecipeCategory)
class RecipeCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')


@admin.register(Assortment)
class AssortimentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')

class DetailsInlineTabularInline(admin.TabularInline):
    model = DetailsInline
    extra = 1

@admin.register(Details)
class DetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_filter = ('id', 'title')
    inlines = (DetailsInlineTabularInline, )

    
@admin.register(Guarantee)
class GuaranteeAdmin(admin.ModelAdmin):
    list_display = ('id', 'delivery_title')
    list_filter = ('id', 'delivery_title')

