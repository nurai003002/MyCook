from django.contrib import admin

from apps.secondary.models import About, AboutInline
# Register your models here.

class AboutInlineTabularInline(admin.TabularInline):
    model = AboutInline
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_filter = ('id', 'title')
    inlines = (AboutInlineTabularInline, )
    