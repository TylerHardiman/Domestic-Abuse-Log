from rest_framework import serializers
from .models import AbuseLog, User

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email' 'user_id']
        depth = 1
        
class AbuseLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbuseLog
        fields = ['id', 'post', 'name', 'email', 'body', 'create_on', 'active', 'user_id']
        depth = 1
