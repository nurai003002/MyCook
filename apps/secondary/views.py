from django.shortcuts import render

from apps.secondary import models
from apps.cms.models import RecipeBanner
# Create your views here.

def video_recipes(request):
    # setting = Setting.objects.latest('id')
    banner = RecipeBanner.objects.latest('id')
    recipe = models.Recipe.objects.all()
    return render(request, 'recipe/recipe_video.html', locals())

def recipe_detail(request, id):
    # setting = Setting.objects.latest('id')
    banner = RecipeBanner.objects.latest('id')
    recipe = models.Recipe.objects.all()
    get_recipe = models.Recipe.objects.get(id=id)
    return render(request, 'recipe/recipe_detail.html', locals())