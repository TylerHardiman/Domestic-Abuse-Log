from django.apps import AppConfig


class SurvivorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'survivor'
    
class AbuseLogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'abuselog'