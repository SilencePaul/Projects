from django.core.management.base import BaseCommand, CommandError
import requests
from lol_website.tasks import get_summoner_info

class Command(BaseCommand):
    help = 'Test function'

    def handle(self, *args, **options):
        get_summoner_info("supermanman")
