from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('games_with_balls/', views.views().games_with_balls, name="games_with_balls"),
    path('bikes/', views.views().bikes, name="bikes"),
    path('dumbbells_and_rods/', views.views().dumbbells_and_rods, name="dumbbells_and_rods"),
    path('fighting_art/', views.views().fighting_art, name="fighting_art"),
    path('premium_attributes/', views.views().premium_attributes, name="premium_attributes"),
    path('billiards/', views.views().billiards, name="billiards"),
    path('jumpers/', views.views().jumpers, name="jumpers"),
    path('desktop_games/', views.views().desktop_games, name="desktop_games"),
    path('baseball/', views.views().baseball, name="baseball"),
    path('espandery/', views.views().espandery, name="espandery"),
    path('swimming/', views.views().swimming, name="swimming"),
    path('darts/', views.views().darts, name="darts"),

]
