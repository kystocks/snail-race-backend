from rest_framework import serializers
from .models import Race


class RaceSerializer(serializers.ModelSerializer):
    """Serializer for individual race results"""
    
    class Meta:
        model = Race
        fields = ['id', 'winner_color', 'race_date', 'total_rolls', 'second_place', 'last_place']
        read_only_fields = ['id', 'race_date']


class RaceStatsSerializer(serializers.Serializer):
    """For aggregate statistics - not tied to a model"""
    red = serializers.IntegerField()
    blue = serializers.IntegerField()
    yellow = serializers.IntegerField()
    green = serializers.IntegerField()
    orange = serializers.IntegerField()
    purple = serializers.IntegerField()
    total_races = serializers.IntegerField()
