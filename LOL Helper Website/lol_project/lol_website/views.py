from django.shortcuts import render
from django.http import HttpResponse

import json

from .models import Champion, ChampionDetail

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

def champion_detail(request, champion_name):
    context = {}
    champion = ChampionDetail.objects.get(champion__search_name=champion_name)
    spells = json.loads(champion.spells)
    passive = json.loads(champion.passive)
    stats = json.loads(champion.stats)
    skins = json.loads(champion.skins)
    allytips = json.loads(champion.allytips)
    enemytips = json.loads(champion.enemytips)
    partytype = champion.partype
    lore = champion.lore

    allytips = [tip.replace("<br>", "") for tip in allytips]
    enemytips = [tip.replace("<br>", "") for tip in enemytips]
    skin_list = []
    skin_url = "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/" + champion.champion.search_name + "_"
    for skin in skins:
        skin_list.append([skin["name"], skin_url + str(skin["num"]) + ".jpg"])

    context["champion"] = champion
    context["skins"] = skin_list
    context["spells"] = spells
    context["passive"] = passive
    context["allytips"] = allytips
    context["enemytips"] = enemytips
    context["lore"] = lore
    context["partytype"] = partytype
    return render(request, 'champion_detail.html', context)
