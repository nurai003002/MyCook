from django.shortcuts import render

from apps.secondary import models
from apps.settings.models import Setting
from apps.cms.models import ProductBanner, Review
# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    about = models.About.objects.latest('id')
    assortment = models.Assortment.objects.all()
    category = models.OwnMyCookCategory.objects.all()
    review = Review.objects.all()
    own_mycook = models.OwnMyCook.objects.all()
    reasons = models.WhyTheyChooseUs.objects.latest('id')
    banner_main = ProductBanner.objects.latest('id')
    return render(request, 'base/index.html', locals())