from django import forms
from main.models import Flower


class SelectBouquet(forms.Form):
    flowers = (Flower.objects.all())
    sel_position = forms.ChoiceField(choices=[(i, f'{i}') for i in range(1, 10)])
    sel_flower = forms.ChoiceField(choices=[(flower.id, f'{flower.name}') for flower in flowers])
    sel_amount = forms.IntegerField(max_value=50, min_value=1)
