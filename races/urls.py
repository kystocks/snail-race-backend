from django.urls import path
from . import views

app_name = 'races'

urlpatterns = [
    path('races/', views.RaceListView.as_view(), name='race_list'),
    path('races/create/', views.RaceCreateView.as_view(), name='race_create'),
    path('stats/', views.race_stats, name='race_stats'),
]
