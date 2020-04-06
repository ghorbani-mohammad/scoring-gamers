from rest_framework import serializers
from gamers.models import Gamer


class GamerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gamer
        fields = ['id', 'mobile', 'score', "rank"]