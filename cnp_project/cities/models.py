from django.db import models


class Continent(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Country(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class City(models.Model):

    name = models.CharField(max_length=200)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    continent = models.ForeignKey('Continent', on_delete=models.CASCADE)
    population = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['name', 'population']

    def __str__(self):
        return self.name
