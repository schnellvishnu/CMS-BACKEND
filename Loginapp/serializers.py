from Loginapp.models import Signinmodel
from rest_framework import serializers

class SigninSerializer(serializers.ModelSerializer):
          class Meta:
                model=Signinmodel
                fields="__all__"                        