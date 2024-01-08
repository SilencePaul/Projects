from lol_website.models import Item, Version

from django.core.management.base import BaseCommand, CommandError
import requests
import json

class Command(BaseCommand):
    help = 'Populates the database with item data from the Riot API'

    def handle(self, *args, **options):
        version = Version.objects.get(id=1).version
        # Get item data from Riot API
        # https://ddragon.leagueoflegends.com/cdn/13.24.1/data/en_US/item.json
        item_response = requests.get(f'http://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/item.json')
        item_data = item_response.json()
        items_data = item_data['data']

        for id in items_data:
            item = items_data[id]
            item_id = id
            if 'name' in item:
                name = item['name']
            else:
                name = None
            if 'description' in item:
                description = item['description']
            else:
                description = None
            if 'plaintext' in item:
                plaintext = item['plaintext']
            else:
                plaintext = None
            if 'image' in item:
                image = item['image']['full']
            else:
                image = None
            if 'gold' in item:
                gold = item['gold']
            else:
                gold = None
            if 'tags' in item:
                tags = json.dumps(item['tags'])
            else:
                tags = None
            if 'stats' in item:
                stats = item['stats']
            else:
                stats = None
            if 'maps' in item:
                maps = item['maps']
            else:
                maps = None
            if 'depth' in item:
                depth = item['depth']
            else:
                depth = None
            if 'into' in item:
                into_item = item['into']
            else:
                into_item = None
            if 'from' in item:
                from_item = item['from']
            else:
                from_item = None
            if 'inStore' in item:
                in_store = item['inStore']
            else:
                in_store = None
            if 'consumed' in item:
                consumed = item['consumed']
            else:
                consumed = None
            if 'specialRecipe' in item:
                special_recipe = item['specialRecipe']
            else:
                special_recipe = None
            if 'requiredAlly' in item:
                required_Ally = item['requiredAlly']
            else:
                required_Ally = None
            if 'requiredChampion' in item:
                required_Champion = item['requiredChampion']
            else:
                required_Champion = None
            
            item = Item.objects.filter(item_id=item_id).first()

            if item is None:
                item = Item(
                            item_id=item_id, 
                            name=name, 
                            description=description, 
                            plaintext=plaintext, 
                            image=image, 
                            gold=gold, 
                            tags=tags, 
                            stats=stats, 
                            maps=maps, 
                            depth=depth, 
                            into_item=into_item, 
                            from_item=from_item, 
                            in_store=in_store, 
                            consumed=consumed, 
                            special_recipe=special_recipe, 
                            required_Ally=required_Ally, 
                            required_Champion=required_Champion
                            )
                item.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully added item {item.name}'))
            else:
                item.name = name
                item.description = description
                item.plaintext = plaintext
                item.image = image
                item.gold = gold
                item.tags = tags
                item.stats = stats
                item.maps = maps
                item.depth = depth
                item.into_item = into_item
                item.from_item = from_item
                item.in_store = in_store
                item.consumed = consumed
                item.special_recipe = special_recipe
                item.required_Ally = required_Ally
                item.required_Champion = required_Champion
                item.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully updated item {item.name}'))
        