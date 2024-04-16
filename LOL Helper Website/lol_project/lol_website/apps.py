from django.apps import AppConfig

class LolWebsiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lol_website'

    def ready(self):
        pass
