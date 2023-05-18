from django.db import models
from django.utils.translation import gettext_lazy as _


class Flower(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name of flower"))
    amount = models.IntegerField(default=0)
    color = models.CharField(max_length=100, verbose_name=_("Color of flower"))
    description = models.TextField(max_length=1000, verbose_name=_("Flower's description"))


class Bouquet(models.Model):
    flowers = models.ManyToManyField(Flower, through="BouquetFlowers")
    description = models.TextField(max_length=1000, verbose_name=_("Bouquet's description"))


class BouquetFlowers(models.Model):
    flowers = models.ForeignKey(Flower, on_delete=models.CASCADE, verbose_name=_("Flower"))
    bouquets = models.ForeignKey(Bouquet, on_delete=models.CASCADE, verbose_name=_("Bouquet"))
    amount = models.IntegerField(default=0)
