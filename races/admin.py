from django.contrib import admin
from .models import Race


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ['winner_color', 'race_date', 'total_rolls']
    list_filter = ['winner_color', 'race_date']
    search_fields = ['winner_color']
    readonly_fields = ['race_date']
