from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password

from authentication.views import Survivor



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, Survivor):
        token = super().get_token(Survivor)

        token["survivorname"] = Survivor.Survivorname
        token["first_name"] = Survivor.first_name
        token["last_name"] = Survivor.last_name
        token["email"] = Survivor.email
        token["password"] = Survivor.pasword
        return token


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[
                                   UniqueValidator(queryset=Survivor.objects.all())])

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = Survivor
        # If added new columns through the Survivor model, add them in the fields
        # list as seen below
        fields = ('survivorname', 'password', 'email',
                  'first_name', 'last_name')

    def create(self, validated_data):

        Survivor = Survivor.objects.create(
            Survivorname=validated_data['survivorname'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password'],
            # If added new columns through the Survivor model, add them in this
            # create method call in the format as seen above
        )
        Survivor.set_password(validated_data['password'])
        Survivor.save()

        return Survivor
