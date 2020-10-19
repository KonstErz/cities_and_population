from django.contrib import admin
from cities.models import Continent, Country, City


class CityInline(admin.TabularInline):
    model = City
    extra = 0


@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    inlines = [CityInline]


@admin.register(Country)
class ContinentAdmin(admin.ModelAdmin):
    inlines = [CityInline]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'continent', 'population')
    list_filter = ('country', 'continent')
