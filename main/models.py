from django.db import models
from django.utils.translation import gettext_lazy as _


class Flower(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name of flower"))
    amount = models.IntegerField(default=0)
    color = models.CharField(max_length=100, verbose_name=_("Color of flower"))
    description = models.TextField(max_length=1000, verbose_name=_("Flower's description"))
    pattern = models.ImageField(null=True, upload_to='', verbose_name=_('Image'))


class Bouquet(models.Model):
    name = models.CharField(default='Букет', max_length=150, verbose_name=_("Bouquet's name"))
    flowers = models.ManyToManyField(Flower, through="BouquetFlowers")
    description = models.TextField(max_length=1000, verbose_name=_("Bouquet's description"))

    def get_absolute_url(self):
        return f'/main/{self.pk}'


class BouquetFlowers(models.Model):
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, verbose_name=_("Flower"))
    bouquet = models.ForeignKey(Bouquet, on_delete=models.CASCADE, verbose_name=_("Bouquet"))
    amount = models.IntegerField(default=0)
    position = models.IntegerField(choices=[(i, i) for i in range(1, 10)], blank=True, null=True)
