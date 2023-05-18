from datetime import date
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=50, verbose_name=_("User's names"))
    last_name = models.CharField(max_length=50, verbose_name=_("User's last names"))
    patronymic = models.CharField(max_length=50, verbose_name=_("User's patronymic"))
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        auto_now=False,
        auto_now_add=False,
        default=date.today
    )
    balance = models.IntegerField(default=0)
    phone = models.CharField(
        validators=[RegexValidator(r'\d{11}', 'Minimum 11', code='invalid')],
        verbose_name="User's phone",
        max_length=18
    )
