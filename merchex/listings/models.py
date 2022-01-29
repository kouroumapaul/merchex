from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator


class Brand(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    name = models.fields.CharField(max_length=100)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField()
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Listing(models.Model):
    class Type(models.TextChoices):
        RECORDS = "Records"
        CLOTHING = "Clothing"
        POSTER = "Poster"
        MISCELLANEOUS = "Miscellaneous"

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=5000)
    is_sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(null=True, blank=True)
    type = models.fields.CharField(choices=Type.choices, max_length=20)
    brand = models.ForeignKey(Brand,on_delete=models.SET_NULL, null=True,)

    def __str__(self):
        return f'{self.title}'

