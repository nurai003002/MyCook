from django.contrib import admin

from apps.cms.models import RecipeBanner, Faqs, FAQsInline, ProductBanner, Review

# Register your models here.
class FAQsInlineTabular(admin.TabularInline):
    model = FAQsInline
    extra = 1

@admin.register(RecipeBanner)
class RecipeBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')
    
@admin.register(Faqs)
class FaqsAdmin(admin.ModelAdmin):
    list_display = ('id', )
    list_filter = ('id', )
    inlines = (FAQsInlineTabular, )
    
@admin.register(ProductBanner)
class ProductBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_filter = ('id', 'text')