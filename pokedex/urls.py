from django.urls import path

from . import views

app_name = "pokedex"

urlpatterns = [
    path("", views.index, name="index"),
    path("pokemon/<int:pokemon_id>/", views.pokemon, name="pokemon"),
    path("add_pokemon/", views.add_pokemon, name="add_pokemon"),
    
    #path("trainer/<int:trainer_id/", views.trainer, name = "trainer")#
]