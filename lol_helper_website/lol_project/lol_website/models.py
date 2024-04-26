from django.utils import timezone
from django.db import models
from django.db.models.fields.json import JSONField

class Champion(models.Model):
    name = models.CharField(max_length=200)
    search_name = models.CharField(max_length=200, default="null")
    title = models.CharField(max_length=200)
    blurb = models.TextField()
    images = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    partype = models.CharField(max_length=200, default="null")
    def __str__(self):
        return self.name
    
class ChampionDetail(models.Model):
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)
    skins = JSONField()
    lore = models.TextField()
    allytips = JSONField()
    enemytips = JSONField()
    tags = JSONField(default=dict)
    partype = models.CharField(max_length=200)
    stats = JSONField()
    spells = JSONField()
    passive = JSONField()
    def __str__(self):
        return self.champion.name
    
class Version(models.Model):
    version = models.CharField(max_length=200)
    def __str__(self):
        return self.version

class Item(models.Model):
    item_id = models.IntegerField(null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    plaintext = models.TextField(null=True)
    image = models.CharField(max_length=200)
    gold = JSONField(null=True)
    tags = models.TextField(null=True)
    stats = JSONField(null=True)
    maps = JSONField(null=True)
    depth = models.IntegerField(null=True)
    into_item = models.TextField(null=True)
    from_item = models.TextField(null=True)
    in_store = models.BooleanField(null=True)
    consumed = models.BooleanField(null=True)
    special_recipe = models.IntegerField(null=True)
    required_Ally = models.CharField(max_length=200, null=True)
    required_Champion = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name
    
class Queue(models.Model):
    queue_id = models.IntegerField()
    map = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True)
    notes = models.CharField(max_length=200, null=True)
    def __str__(self):
        if self.description == None:
            return self.map
        return self.map + "-" + self.description
    
class Map(models.Model):
    map_id = models.IntegerField()
    map_name = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    def __str__(self):
        return self.map_name

class GameMode(models.Model):
    game_mode = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.game_mode
    
class LPHistory(models.Model):
    queueType = models.CharField(max_length=200)
    tier = models.CharField(max_length=200)
    rank = models.CharField(max_length=200)
    summonerName = models.CharField(max_length=200)
    leaguePoints = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    updated_on = models.DateTimeField(default=timezone.now)

class APIKey(models.Model):
    api_key = models.CharField(max_length=200)
    def __str__(self):
        return self.api_key
