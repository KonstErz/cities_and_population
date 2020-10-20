from django.db import models


class Continent(models.Model):
    """
    The Model represents a part of the world,
    for example: America, Europe, Asia, etc.
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Country(models.Model):
    """
    The Model represents a country that belongs to a certain part of the world,
    for example: USA, Russia, France, China, etc.
    """

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class City(models.Model):
    """
    The Model represents a settlement that belongs to a particular country and
    part of the world and has a name and population (thousand people,
    positive integer).
    Sort by default: by name and population.
    """

    name = models.CharField(max_length=200)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    continent = models.ForeignKey('Continent', on_delete=models.CASCADE)
    population = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['name', 'population']

    def __str__(self):
        return self.name
