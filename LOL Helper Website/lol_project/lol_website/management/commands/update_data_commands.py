from lol_website.models import Champion, ChampionDetail, Version

from django.core.management.base import BaseCommand, CommandError
import requests
import json

class Command(BaseCommand):
    help = 'Populates the database with champion data from the Riot API'

    def handle(self, *args, **options):
        version_response = requests.get('https://ddragon.leagueoflegends.com/api/versions.json')
        version_data = version_response.json()
        version = version_data[0]
        # Update version
        version_object = Version.objects.filter(version=version).first()
        if version_object:
            pass
        else:
            version_object = Version(version=version)
            version_object.save()
        # Get champion data from Riot API
        champion_response = requests.get(f'http://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json')
        champion_data = champion_response.json()
        champions_data = champion_data['data']

        for champion_name, champion_info in champions_data.items():
            # Check if champion already exists in database
            champion = Champion.objects.filter(name=champion_info['name']).first()
            if champion:
                champion_detail_response = requests.get(f'http://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion/{champion_name}.json')
                print(champion_detail_response)
                champion_detail_data = champion_detail_response.json()
                champion_detail = ChampionDetail.objects.filter(champion=champion).first()
                if champion_detail:
                    champion_data = champion_detail_data['data'][champion_name]
                    champion_detail.skins = json.dumps(champion_data['skins'])
                    champion_detail.lore = champion_data['lore']
                    champion_detail.allytips = json.dumps(champion_data['allytips'])
                    champion_detail.enemytips = json.dumps(champion_data['enemytips'])
                    champion_detail.tags = json.dumps(champion_data['tags'])
                    champion_detail.partype = champion_data['partype']
                    champion_detail.stats = json.dumps(champion_data['stats'])
                    champion_detail.spells = json.dumps(champion_data['spells'])
                    champion_detail.passive = json.dumps(champion_data['passive'])
                    champion_detail.save()
                else:
                    champion_data = champion_detail_data['data'][champion_name]
                    champion_detail = ChampionDetail(
                        champion=champion,
                        skins=json.dumps(champion_data['skins']),
                        lore=champion_data['lore'],
                        allytips=json.dumps(champion_data['allytips']),
                        enemytips=json.dumps(champion_data['enemytips']),
                        tags=json.dumps(champion_data['tags']),
                        partype=champion_data['partype'],
                        stats=json.dumps(champion_data['stats']),
                        spells=json.dumps(champion_data['spells']),
                        passive=json.dumps(champion_data['passive']))
                    champion_detail.save()
                champion.name = champion_info['name']
                champion.search_name = champion_name
                champion.title = champion_info['title']
                champion.blurb = champion_info['blurb']
                champion.images = json.dumps(champion_info['image']["full"])
                champion.tags = json.dumps(champion_info['tags'])
                champion.partype = champion_info['partype']
                champion.save()
            else:
            # Create champion object
                champion = Champion(
                    name=champion_info['name'], 
                    search_name=champion_name,
                    title=champion_info['title'], 
                    blurb=champion_info['blurb'], 
                    images=json.dumps(champion_info['image']["full"]), 
                    tags=json.dumps(champion_info['tags']), 
                    partype=champion_info['partype'])
                champion.save()
                champion_detail_response = requests.get(f'http://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion/{champion_name}.json')
                champion_detail_data = champion_detail_response.json()
                champion_data = champion_detail_data['data'][champion_name]
                champion_detail = ChampionDetail(
                    champion=champion,
                    skins=json.dumps(champion_data['skins']),
                    lore=champion_data['lore'],
                    allytips=json.dumps(champion_data['allytips']),
                    enemytips=json.dumps(champion_data['enemytips']),
                    tags=json.dumps(champion_data['tags']),
                    partype=champion_data['partype'],
                    stats=json.dumps(champion_data['stats']),
                    spells=json.dumps(champion_data['spells']),
                    passive=json.dumps(champion_data['passive']))
                champion_detail.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated champion data'))

