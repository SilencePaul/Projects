from django.contrib import admin

from .models import Champion, ChampionDetail, Version

admin.site.register(Champion)
admin.site.register(ChampionDetail)
admin.site.register(Version)
