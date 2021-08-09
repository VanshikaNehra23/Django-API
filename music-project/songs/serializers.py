from rest_framework import serializers
from .models import Songs

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ('name','singer','genre')

class SongSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ('name',)