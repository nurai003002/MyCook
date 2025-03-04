from django.shortcuts import render

from apps.secondary import models

# Create your views here.
def index(request):
    about = models.About.objects.latest('id')
    assortiment = models.Assortment.objects.all()
    details = models.Details.objects.latest('id')
    details_inline = models.DetailsInline.objects.all()
    return render(request, 'base/index.html', locals())
