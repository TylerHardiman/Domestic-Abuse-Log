from django.contrib import admin
from drf_jwt_backend.users.models import Survivor, AbuseLog

# Register your models here.
admin.site.register(Survivor)
admin.site.register(AbuseLog)
