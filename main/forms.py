from django import forms
from main.models import Flower, Bouquet


class SelectBouquet(forms.Form):

    flowers = (Flower.objects.all())
    sel_position = forms.ChoiceField(choices=[(i, f'{i}') for i in range(1, 10)])
    sel_flower = forms.ChoiceField(choices=[(flower.id, f'{flower.name}') for flower in flowers])
    sel_amount = forms.IntegerField(max_value=50, min_value=1)


class ChangeBouquetInfo(forms.Form):
    set_name = forms.CharField(max_length=100)
    set_description = forms.CharField(max_length=200)

