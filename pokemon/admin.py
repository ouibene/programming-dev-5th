from django.contrib import admin
from pokemon.models import Pokemon
from pokemon.models import Place
from pokemon.models import Person

# Register your models here.
class PokemonAdmin(admin.ModelAdmin):
    list_display = ["name", "captured_date", "person"]

class PlaceAdmin(admin.ModelAdmin):
    list_display = ["name", "lnglat"]

class PersonAdmin(admin.ModelAdmin):
    list_display = ["name", "level"]


admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Person, PersonAdmin)