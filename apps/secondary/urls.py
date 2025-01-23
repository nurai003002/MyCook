from django.urls import path

from apps.secondary import views

urlpatterns = [
    path('video-recipes', views.video_recipes, name='video_recipes')
]