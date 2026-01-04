from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
from .models import Race
from .serializers import RaceSerializer, RaceStatsSerializer


class RaceListView(generics.ListAPIView):
    """GET /api/races/ - List all races"""
    queryset = Race.objects.all()
    serializer_class = RaceSerializer


class RaceCreateView(generics.CreateAPIView):
    """POST /api/races/create/ - Save a new race result"""
    queryset = Race.objects.all()
    serializer_class = RaceSerializer


@api_view(['GET'])
def race_stats(request):
    """GET /api/stats/ - Aggregate win counts by color"""
    
    # Count wins by color
    stats = Race.objects.values('winner_color').annotate(count=Count('winner_color'))
    
    # Initialize all colors to 0
    color_counts = {
        'red': 0,
        'blue': 0,
        'yellow': 0,
        'green': 0,
        'orange': 0,
        'purple': 0,
    }
    
    # Fill in actual counts
    for stat in stats:
        color_counts[stat['winner_color']] = stat['count']
    
    color_counts['total_races'] = Race.objects.count()
    
    serializer = RaceStatsSerializer(color_counts)
    return Response(serializer.data)
