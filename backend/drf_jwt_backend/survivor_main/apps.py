from django.apps import AppConfig

from backend.drf_jwt_backend.settings import DEFAULT_AUTO_FIELD


class SuvrivorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Survivor'
    
class AbuseLogConfig(AppConfig):
    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
    name = 'AbuseLog'