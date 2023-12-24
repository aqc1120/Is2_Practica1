from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(
        unique=True,
        null = False,
        blank = False,
        max_length=50
    )
    description = models.TextField(
        max_length=2000,
        null = False,
        blank = False
    )
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.name

class Cruise(models.Model):
    name = models.CharField(
        unique=True,
        null = False,
        blank = False,
        max_length=50
    )
    description = models.TextField(
        max_length=2000,
        null = False,
        blank = False
    )
    destination = models.ManyToManyField(
        Destination,
        related_name='destinations'
    )
    def __str__(self) -> str:
        return self.name
    

class Review(models.Model):
    name = models.CharField(
        unique=False,
        null = False,
        blank = False,
        max_length=50
    )
    review = models.TextField(
        unique=False,
        max_length=2000,
        null = False,
        blank = False
    )
    email = models.TextField(
        unique=False,
        max_length=254,
        null = False,
        blank = False,
    )
    def __str__(self) -> str:
        return self.name