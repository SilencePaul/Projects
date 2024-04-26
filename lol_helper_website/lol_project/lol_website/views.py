from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.core.serializers import serialize
from django.core.management import call_command

import json

import requests

from .models import *

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
    starter_items = []
    consumable_items = []
    distributed_items = []
    trinket_items = []
    boots_items = []
    basic_items = []
    epic_items = []
    legendary_items = []
    ornn_items = []
    champion_exclusive_items = []
    minion_and_turret_items = []

    for item in items:
        images[item.item_id] = images_url + item.image
        item_to_name[item.item_id] = item.name
        if item.maps["11"] == False:
            off_store_items.append(item.item_id)
        elif item.maps["11"] == True:
            in_store_items.append(item.item_id)

    for item in items:
        tags = json.loads(item.tags)
        if "Consumable" in tags and (item.maps.get("11") is True or item.maps.get("12") is True) and item.in_store != False and item.required_Champion == None:
            consumable_items.append(item.item_id)

    for item in items:
        if item.consumed == True and item.in_store == False and (item.maps.get("11") is True or item.maps.get("12") is True) and item.required_Champion == None:
            distributed_items.append(item.item_id)
    
    for item in items:
        tags = json.loads(item.tags)
        if "Trinket" in tags and (item.maps.get("11") is True or item.maps.get("12") is True):
            trinket_items.append(item.item_id)

    for item in items:
        tags = json.loads(item.tags)
        if "Boots" in tags and (item.maps.get("11") is True or item.maps.get("12") is True):
            boots_items.append(item.item_id)

    for item in items:
        tags = json.loads(item.tags)
        if ("Lane" in tags and (item.maps.get("11") is True or item.maps.get("12") is True)) or ("Jungle" in tags and (item.maps.get("11", False) or item.maps.get("12", False))):
            if item.into_item == None and item.from_item == None and item.in_store != False:
                if item.item_id not in trinket_items and item.item_id not in consumable_items and item.item_id not in trinket_items:
                    starter_items.append(item.item_id)
    
    for item in items:
        if item.from_item == None and item.in_store != False and item.required_Champion == None:
            if item.maps.get("11") is True or item.maps.get("12") is True:
                if item.item_id not in trinket_items and item.item_id not in consumable_items and item.item_id not in trinket_items and item.item_id not in starter_items:
                    basic_items.append(item.item_id)
    
    for item in items:
        if item.from_item != None and item.in_store != False and item.required_Champion == None and item.into_item != None:
            if item.maps.get("11") is True or item.maps.get("12") is True:
                try:
                    intos = json.loads(item.into_item)
                    if intos[0] < "7000" or len(intos) > 1:
                        epic_items.append(item.item_id)
                except:
                    print("Failed to decode", item.name, item.item_id)
    
    for item in items:
        if item.from_item != None and item.in_store != False and item.required_Champion == None:
            if item.maps.get("11") is True or item.maps.get("12") is True:
                if item.item_id not in epic_items and item.item_id not in boots_items and item.item_id not in starter_items and item.item_id not in trinket_items and item.item_id not in consumable_items and item.item_id not in trinket_items:
                    if item.into_item == None:
                        legendary_items.append(item.item_id)
                    else:
                        try:
                            intos = json.loads(item.into_item)
                            if len(intos[0]) == 1 and  intos[0] > "7000":
                                legendary_items.append(item.item_id)
                        except:
                            print("Failed to decode", item.name, item.item_id)
    
    for item in items:
        if item.required_Ally == "Ornn" and item.in_store != False:
            if item.maps.get("11") is True or item.maps.get("12") is True:
                ornn_items.append(item.item_id)

    for item in items:
        if item.required_Champion != None:
            if item.maps.get("11") is True or item.maps.get("12") is True:
                champion_exclusive_items.append(item.item_id)
    
    for item in items:
        if item.maps.get("11") is True or item.maps.get("12") is True:
            if item.in_store == False and item.into_item == None and item.from_item == None:
                if item.item_id not in trinket_items and item.item_id not in consumable_items and item.item_id not in trinket_items and item.item_id not in starter_items and item.item_id not in epic_items and item.item_id not in legendary_items and item.item_id not in ornn_items and item.item_id not in champion_exclusive_items:
                    if item.item_id not in distributed_items and item.special_recipe == None:
                        if item.name != "Structure Bounty":
                            minion_and_turret_items.append(item.item_id)
    
    context["starter_items"] = starter_items
    context["consumable_items"] = consumable_items
    context["distributed_items"] = distributed_items
    context["trinket_items"] = trinket_items
    context["boots_items"] = boots_items
    context["basic_items"] = basic_items
    context["epic_items"] = epic_items
    context["legendary_items"] = legendary_items
    context["ornn_items"] = ornn_items
    context["champion_exclusive_items"] = champion_exclusive_items
    context["minion_and_turret_items"] = minion_and_turret_items
    context["images"] = images
    context["items"] = items
    context["item_to_name"] = item_to_name
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

def lp(request):
    context = {}
    lp_history_supermanman_solo = LPHistory.objects.filter(Q(queueType="RANKED_SOLO_5x5")
                                        & Q(summonerName="supermanman")).order_by("updated_on")
    lp_history_supermanman_flex = LPHistory.objects.filter(Q(queueType="RANKED_FLEX_SR")
                                        & Q(summonerName="supermanman")).order_by("updated_on")
    lp_history_biaoge_flex = LPHistory.objects.filter(Q(queueType="RANKED_FLEX_SR")
                                        & Q(summonerName="BiaoGe")).order_by("updated_on")

    context["lp_history_supermanman_solo"] = lp_history_supermanman_solo
    context["lp_history_supermanman_flex"] = lp_history_supermanman_flex
    context["lp_history_biaoge_flex"] = lp_history_biaoge_flex
    return render(request, 'lp_history.html', context)

def updates(request):
    context = {}
    messages = []
    if request.method == "POST":
        api_key = request.POST.get("api_key")
        champion_data = request.POST.get("champion_data")
        item_data = request.POST.get("item_data")
        if champion_data == "true":
            call_command("champion_data_update")
            messages.append("Champion Data Updated")
        if item_data == "true":
            call_command("item_data_update")
            messages.append("Item Data Updated")
        response = requests.get(f'https://na1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key={api_key}')
        response_json = response.json()
        if response_json["status"]["status_code"] == 403:
            message = "API Key is invalid"
            context["error_message"] = message
            return render(request, 'updates.html', context)
        else:
            APIKey.objects.all().delete()
            new_api_key = APIKey(api_key=api_key)
            new_api_key.save()
            messages.append("API Key Updated")
        context["messages"] = messages
    return render(request, 'updates.html', context)