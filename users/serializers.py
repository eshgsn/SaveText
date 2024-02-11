# import serializer from rest_framework
from rest_framework import serializers
 
# import model from models.py
from .models import UserData
 
# Create a model serializer
class UserDataSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = UserData
        fields = ( 'fileName','textFile','ownerUserId')