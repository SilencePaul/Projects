from django.contrib import admin

from .models import Champion, ChampionDetail, LPHistory, Version, Item, Queue, Map, GameMode


class ChampionAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'search_name')
    search_fields = ['name', 'title', 'search_name']

class ChampionDetailAdmin(admin.ModelAdmin):
    list_display = ('champion', 'partype')
    search_fields = ['champion', 'partype']

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'item_id')
    search_fields = ['name', 'item_id']

class LPHistoryAdmin(admin.ModelAdmin):
    list_display = ('summonerName', 'queueType', 'tier', 'rank', 'leaguePoints', 'wins', 'losses')
    search_fields = ['summonerName', 'queueType', 'tier', 'rank', 'leaguePoints', 'wins', 'losses']
    list_filter = ['queueType']
    ordering = ('-updated_on',)

admin.site.register(LPHistory, LPHistoryAdmin)
admin.site.register(Champion, ChampionAdmin)
admin.site.register(ChampionDetail, ChampionDetailAdmin)
admin.site.register(Version)
admin.site.register(Item, ItemAdmin)
admin.site.register(Queue)
admin.site.register(Map)
admin.site.register(GameMode)