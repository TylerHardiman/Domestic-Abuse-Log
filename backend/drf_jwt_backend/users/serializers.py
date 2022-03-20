from rest_framework import serializers
from users.models import AbuseLog, Survivor

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class SurvivorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survivor
        fields = ['id', 'first_name', 'last_name', 'email' 'survivor_id']
        depth = 1
        
class AbuseLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbuseLog
        fields = ['post', 'name', 'email', 'body', 'create_on', 'active', 'survivor_id']
        depth = 1
