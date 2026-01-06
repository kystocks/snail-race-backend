from django.db import models
from .constants import SNAIL_COLORS


class Race(models.Model):
    """Stores the result of a single snail race"""
    
    winner_color = models.CharField(max_length=20, choices=SNAIL_COLORS)
    race_date = models.DateTimeField(auto_now_add=True)
    
    # Optional fields for Phase 2.5
    total_rolls = models.IntegerField(null=True, blank=True)
    second_place = models.CharField(max_length=20, choices=SNAIL_COLORS, null=True, blank=True)
    last_place = models.CharField(max_length=20, choices=SNAIL_COLORS, null=True, blank=True)
    
    class Meta:
        ordering = ['-race_date']  # Newest first
    
    def __str__(self):
        return f"{self.winner_color} won on {self.race_date.strftime('%Y-%m-%d %H:%M')}"
