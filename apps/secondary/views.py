from django.shortcuts import render

from apps.secondary import models
from apps.cms.models import RecipeBanner, Faqs
from apps.settings.models import Setting
# Create your views here.

def video_recipes(request):
    setting = Setting.objects.latest('id')
    category_id = request.GET.get('category_id')
    banner = RecipeBanner.objects.latest('id')
    categories = models.RecipeCategory.objects.all()
    
    if category_id:
        recipe = models.Recipe.objects.filter(category_id=category_id) 
    else:
        recipe = models.Recipe.objects.all()
        
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render(request, 'recipe/partials/recipe_list.html', {'recipe': recipe})
    
    return render(request, 'recipe/recipe_video.html', locals())


def recipe_detail(request, id):
    setting = Setting.objects.latest('id')
    banner = RecipeBanner.objects.latest('id')
    recipe = models.Recipe.objects.all()
    get_recipe = models.Recipe.objects.get(id=id)
    return render(request, 'recipe/recipe_detail.html', locals())


def guarentee(request):
    setting = Setting.objects.latest('id')
    banner = RecipeBanner.objects.latest('id')
    guarentees = models.Guarantee.objects.latest('id')
    return render(request, 'secondary/guarentee.html', locals())

def faqs(request):
    setting = Setting.objects.latest('id')
    faqs = Faqs.objects.latest('id')
    banner = RecipeBanner.objects.latest('id')
    return render(request, 'secondary/faqs.html', locals())