from django.shortcuts import render, redirect
from telebot import TeleBot

from apps.secondary import models
from apps.telegram_bot.views import get_text
from apps.settings.models import Setting, Contact
from apps.cms.models import ProductBanner, Review, RecipeBanner, UrlWhatsapp
# Create your views here.

def index(request):
    setting = Setting.objects.latest('id')
    about = models.About.objects.latest('id')
    assortment = models.Assortment.objects.all()
    category = models.OwnMyCookCategory.objects.all()
    review = Review.objects.all()
    review_count = review.count()
    own_mycook = models.OwnMyCook.objects.all()
    reasons = models.WhyTheyChooseUs.objects.latest('id')
    banner_main = ProductBanner.objects.latest('id')
    url = UrlWhatsapp.objects.latest('id')
    return render(request, 'base/index.html', locals())

def about(request):
    setting = Setting.objects.latest('id')
    about = models.About.objects.latest('id')
    banner = RecipeBanner.objects.latest('id')
    team = models.Team.objects.all()
    return render(request, 'base/about.html', locals())

def contact(request):
    setting = Setting.objects.latest('id')
    banner = RecipeBanner.objects.latest('id')
    url = UrlWhatsapp.objects.latest('id')
    if 'contact' in request.POST:
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        page_contact = Contact.objects.create(name=name, phone=phone, message=message)
        if page_contact:
            get_text(f"""
            Оставлена заявка на обратный звонок 📞
                         
Имя пользователя:  {name}
Почта: {phone}
Сообщение: {message}
            """)
            return redirect('index')

    return render(request, 'base/contact.html', locals())