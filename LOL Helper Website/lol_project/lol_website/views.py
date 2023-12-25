from django.shortcuts import render
from django.http import HttpResponse

from .models import Champion

def index(request):
    context = {}
    champions = Champion.objects.all()
    images_url = "https://ddragon.leagueoflegends.com/cdn/img/champion/loading/"
    images_url_end = "_0.jpg"
    images = {}
    for champion in champions:
        images[champion.search_name] = images_url + champion.search_name + images_url_end
    context["images"] = images
    context["champions"] = champions
    return render(request, 'index.html', context)

def champions(request):
    context = {}
    champions = Champion.objects.all()
    images_url = "https://ddragon.leagueoflegends.com/cdn/img/champion/loading/"
    images_url_end = "_0.jpg"
    images = {}
    for champion in champions:
        images[champion.search_name] = images_url + champion.search_name + images_url_end
    context["images"] = images
    context["champions"] = champions
    return render(request, 'champions.html', context)
