from rest_framework import serializers
from .models import Survivor

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class SurvivorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survivor
        fields = ['id', 'warrior', 'email', 'datetime', 'user_id']
        depth = 1
        
class AbuseLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survivor
        fields = ['id', 'warrior', 'email', 'datetime', 'user_id']
        depth = 1
