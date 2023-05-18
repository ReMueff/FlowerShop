from django.db import models
from django.utils.translation import gettext_lazy as _
from main.models import Bouquet
from users.models import User


class Items(models.Model):
    class Status(models.TextChoices):
        CART = 'CART', _('In cart')
        AWAITING_ARRIVAL = 'AWAITING_ARRIVAL', _('Awaiting_arrival')
        AWAITING_PAYMENT = 'AWAITING_PAYMENT', _('Awaiting payment')
        PAID = 'PAID', _('Paid')
        AWAITING_DELIVERY = 'AWAITING_DELIVERY', _('Awaiting delivery')
        SENT = 'SENT', _('Sent')
        FINISHED = 'FINISHED', _('Finished')

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    bouquet = models.ForeignKey(Bouquet, on_delete=models.CASCADE, verbose_name=_("Bouquet"))
    status = models.CharField(max_length=100, verbose_name=_("Status"))
