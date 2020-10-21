from django.contrib import admin
from cities.models import Continent, Country, City


class CityInline(admin.TabularInline):
    """
    Used to display cities in the row below linked cities with
    continents and countries.
    """

    model = City
    extra = 0


@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    """
    Administration object for Continent models.
    Adds inline addition of cities in continent view (inlines).
    Active search box on the list page by the field 'name'.
    """

    search_fields = ['name']
    inlines = [CityInline]


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """
    Administration object for Country models.
    Adds inline addition of cities in country view (inlines).
    Active search box on the list page by the field 'name'.
    """

    search_fields = ['name']
    inlines = [CityInline]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """
    Administration object for City models.
    Defines:
        - fields to be displayed in list view (list_display)
        - grouping fields horizontally with the ability to sort by field
        - adds cities filters by country and continent
        - search box on the list page by fields: name, country and continent
    """

    list_display = ('name', 'country', 'continent', 'population')
    list_filter = ('country', 'continent')
    search_fields = ['name', 'country__name', 'continent__name']
