from lol_website.models import Item, Version

from django.core.management.base import BaseCommand, CommandError
import requests
import json

class Command(BaseCommand):
    help = 'Populates the database with item data from the Riot API'

    def handle(self, *args, **options):
        version = Version.objects.all().order_by("id").last().version
        # Get item data from Riot API
        
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
                depth = 0
            if 'into' in item:
                into_item = json.dumps(item['into'])
            else:
                into_item = None
            if 'from' in item:
                from_item = json.dumps(item['from'])
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
            
            item_check = Item.objects.filter(item_id=item_id).first()

            if item_check is None:
                item_check = Item(
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
                item_check.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully added item {item_check.name}'))
            else:
                item_check.name = name
                item_check.description = description
                item_check.plaintext = plaintext
                item_check.image = image
                item_check.gold = gold
                item_check.tags = tags
                item_check.stats = stats
                item_check.maps = maps
                item_check.depth = depth
                item_check.into_item = into_item
                item_check.from_item = from_item
                item_check.in_store = in_store
                item_check.consumed = consumed
                item_check.special_recipe = special_recipe
                item_check.required_Ally = required_Ally
                item_check.required_Champion = required_Champion
                item_check.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully updated item {item_check.name}'))
        