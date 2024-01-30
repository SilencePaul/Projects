from django.shortcuts import render
from django.http import HttpResponse

import json

from .models import Champion, ChampionDetail, Item, Version

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
    champions = Champion.objects.all().order_by("name")
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
    tags = json.loads(champion.tags)
    partytype = champion.partype
    lore = champion.lore

    allytips = [tip.replace("<br>", "") for tip in allytips]
    enemytips = [tip.replace("<br>", "") for tip in enemytips]
    skin_list = []
    skin_url = "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/" + champion.champion.search_name + "_"
    for skin in skins:
        skin_list.append([skin["name"], skin_url + str(skin["num"]) + ".jpg"])

    skin_count = len(skin_list)
    images_url = "https://ddragon.leagueoflegends.com/cdn/img/champion/loading/"
    images_url_end = "_0.jpg"
    loading_image = images_url + champion.champion.search_name + images_url_end

    version = Version.objects.all().order_by("id").last().version
    spells_url = "https://ddragon.leagueoflegends.com/cdn/" + version + "/img/spell/"
    passive_url = "https://ddragon.leagueoflegends.com/cdn/" + version + "/img/passive/"
    for spell in spells:
        spell["image"] = spells_url + spell["image"]["full"]
    passive["image"] = passive_url + passive["image"]["full"]    

    context["champion"] = champion
    context["loading_image"] = loading_image
    context["skins"] = skin_list
    context["spells"] = spells
    context["stats"] = stats
    context["passive"] = passive
    context["allytips"] = allytips
    context["enemytips"] = enemytips
    context["tags"] = tags
    context["lore"] = lore
    context["partytype"] = partytype
    context["skin_count"] = skin_count
    return render(request, 'champion_detail.html', context)

def items(request):
    context = {}
    items = Item.objects.all()
    version = Version.objects.all().order_by("id").last().version
    images_url = "https://ddragon.leagueoflegends.com/cdn/" + version + "/img/item/"
    images = {}
    item_to_name = {}
    in_store_items = []
    off_store_items = []
    for item in items:
        images[item.item_id] = images_url + item.image
        item_to_name[item.item_id] = item.name
        if item.maps["11"] == False:
            off_store_items.append(item.item_id)
        elif item.maps["11"] == True:
            in_store_items.append(item.item_id)
    
    context["in_store_items"] = in_store_items
    context["off_store_items"] = off_store_items
    context["item_to_name"] = item_to_name

    tags_list = []
    for item in items:
        tags = json.loads(item.tags)
        for tag in tags:
            if tag not in tags_list:
                tags_list.append(tag)
    
    context["tags"] = tags_list
    context["images"] = images
    context["items"] = items
    return render(request, 'items.html', context)

def item_detail(request, item_id):
    context = {}
    item = Item.objects.get(item_id=item_id)
    version = Version.objects.all().order_by("id").last().version
    images_url = "https://ddragon.leagueoflegends.com/cdn/" + version + "/img/item/"
    image = images_url + item.image
    context["image"] = image
    context["item"] = item
    return render(request, 'item_detail.html', context)