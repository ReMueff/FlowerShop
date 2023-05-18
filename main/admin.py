from django.contrib import admin

from main.models import Bouquet, Flower, BouquetFlowers

# Register your models here.

admin.site.register(Flower)
admin.site.register(Bouquet)
admin.site.register(BouquetFlowers)
