from rest_framework import serializers
from .models import AbuseLog
from .models import Survivor

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class SurvivorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survivor
        fields = ['id', 'user', 'first_name', 'last_name', 'email' 'user_id']
        depth = 1
        
class AbuseLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbuseLog
        fields = ['post', 'name', 'email', 'body', 'create_on', 'active', 'user_id']
        depth = 1
