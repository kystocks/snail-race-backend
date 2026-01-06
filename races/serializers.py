from rest_framework import serializers
from .models import Race


class RaceSerializer(serializers.ModelSerializer):
    """Serializer for individual race results"""
    
    class Meta:
        model = Race
        fields = ['id', 'winner_color', 'race_date', 'total_rolls', 'second_place', 'last_place']
        read_only_fields = ['id', 'race_date']
    
    def validate_winner_color(self, value):
        """Validate that winner_color is one of the valid snail colors"""
        valid_colors = [color[0] for color in Race.SNAIL_COLORS]
        if value not in valid_colors:
            raise serializers.ValidationError(
                f"Invalid color '{value}'. Must be one of: {', '.join(valid_colors)}"
            )
        return value
    
    def validate_second_place(self, value):
        """Validate that second_place is one of the valid snail colors"""
        if value is None:
            return value
        valid_colors = [color[0] for color in Race.SNAIL_COLORS]
        if value not in valid_colors:
            raise serializers.ValidationError(
                f"Invalid color '{value}'. Must be one of: {', '.join(valid_colors)}"
            )
        return value
    
    def validate_last_place(self, value):
        """Validate that last_place is one of the valid snail colors"""
        if value is None:
            return value
        valid_colors = [color[0] for color in Race.SNAIL_COLORS]
        if value not in valid_colors:
            raise serializers.ValidationError(
                f"Invalid color '{value}'. Must be one of: {', '.join(valid_colors)}"
            )
        return value
    
    def validate_total_rolls(self, value):
        """Validate that total_rolls is a positive integer"""
        if value is not None and value < 1:
            raise serializers.ValidationError("Total rolls must be at least 1")
        return value
    
    def validate(self, data):
        """Cross-field validation to ensure colors are different"""
        winner = data.get('winner_color')
        second = data.get('second_place')
        last = data.get('last_place')
        
        # Check if winner and last place are the same
        if winner and last and winner == last:
            raise serializers.ValidationError(
                "Winner and last place cannot be the same color"
            )
        
        # Check if winner and second place are the same
        if winner and second and winner == second:
            raise serializers.ValidationError(
                "Winner and second place cannot be the same color"
            )
        
        # Check if second and last place are the same
        if second and last and second == last:
            raise serializers.ValidationError(
                "Second place and last place cannot be the same color"
            )
        
        return data


class RaceStatsSerializer(serializers.Serializer):
    """For aggregate statistics - not tied to a model"""
    red = serializers.IntegerField()
    blue = serializers.IntegerField()
    yellow = serializers.IntegerField()
    green = serializers.IntegerField()
    orange = serializers.IntegerField()
    purple = serializers.IntegerField()
    total_races = serializers.IntegerField()
