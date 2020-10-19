from django.shortcuts import render
from django_tables2 import RequestConfig
from cities.models import City, Continent
from cities.tables import CityTable


def city_list(request):
    config = RequestConfig(request)
    continents = Continent.objects.all().order_by('name')
    tables = [CityTable(City.objects.filter(continent=continent),
                        prefix=continent.name) for continent in continents]

    for table in tables:
        config.configure(table)

    return render(request, 'cities/city_list.html', {
        'tables': tables,
    })
