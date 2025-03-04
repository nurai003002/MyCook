from django.urls import path

from apps.secondary import views

urlpatterns = [
    path('video-recipes/', views.video_recipes, name='video_recipes'),
    path('video-detail/<int:id>/', views.recipe_detail, name='recipe_detail'),
    path('guarentee/', views.guarentee, name='guarentee'),
    path('faqs/', views.faqs, name='faqs')
]