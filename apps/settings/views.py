from django.shortcuts import render

from apps.secondary import models
from apps.settings.models import Setting
# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    about = models.About.objects.latest('id')
    return render(request, 'base/index.html', locals())