from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.password_validation import validate_password
from users.models import Survivor



class MyTokenObtainPairSerializer(TokenAuthentication):
    @classmethod
    def get_token(cls, survivor):
        token = super().get_token(survivor)

        token["survivorname"] = survivor.survivorname
        token["first_name"] = survivor.first_name
        token["last_name"] = survivor.last_name
        token["email"] = survivor.email
        token["password"] = survivor.password
        return token


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[
                                   UniqueValidator(queryset=Survivor.objects.all())])

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = Survivor
        # If added new columns through the survivor model, add them in the fields
        # list as seen below
        fields = ('survivorname', 'password', 'email',
                  'first_name', 'last_name')

    def create(self, validated_data):

        survivor = Survivor.objects.create(
            survivorname=validated_data['survivorname'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            # If added new columns through the survivor model, add them in this
            # create method call in the format as seen above
        )
        survivor.set_password(validated_data['password'])
        survivor.save()

        return survivor
