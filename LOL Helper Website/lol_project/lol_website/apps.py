from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
import os

def test_working():
    print("working")

def start():
    from .tasks import get_summoner_info
    get_summoner_info("supermanman")
    get_summoner_info("Biaoge")
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_summoner_info, 'interval', minutes=30, args=["supermanman"])
    scheduler.add_job(get_summoner_info, 'interval', minutes=30, args=["Biaoge"])
    scheduler.start()

class LolWebsiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lol_website'

    def ready(self):
        if os.environ.get('RUN_MAIN') == 'true':
            print("Starting scheduler...")
            start()
