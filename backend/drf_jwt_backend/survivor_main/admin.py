from django.contrib import admin
from .models import Survivor
from .models import AbuseLog

# Register your models here.
admin.site.register(Survivor)
admin.site.register(AbuseLog)
