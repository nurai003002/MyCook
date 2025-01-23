from django.shortcuts import render

# Create your views here.

def video_recipes(request):
    # setting = Setting.objects.latest('id')
    return render(request, 'video/video-gallery.html', locals())