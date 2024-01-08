from lol_website.models import Map, GameMode, Queue

from django.core.management.base import BaseCommand, CommandError
import requests

class Command(BaseCommand):
    help = 'Populates the database with map and game mode data from the Riot API'

    def handle(self, *args, **options):
        queue_response = requests.get(f'https://static.developer.riotgames.com/docs/lol/queues.json')
        queue_data = queue_response.json()
        for queue in queue_data:
            queue_id = queue['queueId']
            queue_map = queue['map']
            queue_description = queue['description']
            queue_notes = queue['notes']
            queue_object = Queue.objects.filter(queue_id=queue_id).first()
            if queue_object:
                pass
            else:
                queue_object = Queue(queue_id=queue_id, map=queue_map, description=queue_description, notes=queue_notes)
                queue_object.save()

        map_response = requests.get(f'https://static.developer.riotgames.com/docs/lol/maps.json')
        map_data = map_response.json()
        for map in map_data:
            map_id = map['mapId']
            map_name = map['mapName']
            map_notes = map['notes']
            map_object = Map.objects.filter(map_id=map_id).first()
            if map_object:
                pass
            else:
                map_object = Map(map_id=map_id, map_name=map_name, notes=map_notes)
                map_object.save()
        
        game_mode_response = requests.get(f'https://static.developer.riotgames.com/docs/lol/gameModes.json')
        game_mode_data = game_mode_response.json()
        for game_mode in game_mode_data:
            game_mode_name = game_mode['gameMode']
            game_mode_description = game_mode['description']
            game_mode_object = GameMode.objects.filter(game_mode=game_mode_name).first()
            if game_mode_object:
                pass
            else:
                game_mode_object = GameMode(game_mode=game_mode_name, description=game_mode_description)
                game_mode_object.save()
        
        