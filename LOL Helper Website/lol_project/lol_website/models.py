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
