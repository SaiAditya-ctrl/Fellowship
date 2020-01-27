from rest_framework import serializers
from . models import Register


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields=['username','email','desc']
class RegisterCreate(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields='__all__'
