from django.urls import path
from cities.views import city_list


urlpatterns = [
    path('', city_list, name='cities'),
]
