from django.contrib import admin

from .models import Champion, ChampionDetail, Version, Item, Queue, Map, GameMode

admin.site.register(Champion)
admin.site.register(ChampionDetail)
admin.site.register(Version)
admin.site.register(Item)
admin.site.register(Queue)
admin.site.register(Map)
admin.site.register(GameMode)
