from django.contrib import admin

from apps.cms.models import RecipeBanner

# Register your models here.

@admin.register(RecipeBanner)
class RecipeBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')
    