from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Thing(models.Model):
    name = models.CharField(unique=True, blank=False, max_length=30),
    description = models.CharField(unique=False, blank=True, max_length=120),
    quantity = models.PositiveSmallIntegerField(unique=False, default=1,
         validators=[MaxValueValidator(100), MinValueValidator(0)])