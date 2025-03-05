from django.contrib import admin

from apps.settings.models import Setting,About, AboutInline

# Register your models here.
class AboutTabularInline(admin.TabularInline):
    model = AboutInline
    extra = 1

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')
    
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')
    inlines = (AboutTabularInline, )
    