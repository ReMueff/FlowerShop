from django import forms
from django.shortcuts import redirect
from django.views.generic import ListView, FormView
from django.views.generic import TemplateView
from django.views.generic import DetailView

from .forms import SelectBouquet
from .models import Bouquet, BouquetFlowers, Flower


class MainPage(ListView):
    template_name = "index.html"
    model = Bouquet
    context_object_name = 'bouquet'

    def get_queryset(self):
        return Bouquet.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['bouquet_list'] = self.get_queryset()
        return context


class Reviewer(FormView):
    template_name = "review.html"
    model = BouquetFlowers
    context_object_name = 'bouquet'
    form_class = SelectBouquet

    def get_queryset(self):
        return BouquetFlowers.objects.filter(bouquet_id=self.kwargs.get('pk'))

    def get_flowers_position(self):
        positions_info = {}
        flowers_info = BouquetFlowers.objects.filter(bouquet_id=self.kwargs.get('pk'))
        for flower_info in flowers_info:
            pattern = Flower.objects.get(id=flower_info.flower_id).pattern
            positions_info[f'{flower_info.position}'] = pattern

        return positions_info

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['positions'] = self.get_flowers_position()
        print(context['positions'])
        context['range'] = range(1, 10)
        context['open_tr'] = (1, 4, 7)
        context['close_tr'] = (3, 6, 9)
        return context

    def post(self, request, *args, **kwargs):
        id_bouquet = self.kwargs.get('pk')
        position = int(request.POST.get('sel_position'))
        flower_id = int(request.POST.get('sel_flower'))
        amount = int(request.POST.get('sel_amount'))
        instance, created = BouquetFlowers.objects.get_or_create(bouquet_id=id_bouquet, position=position)

        instance.flower_id = flower_id
        instance.amount = amount
        instance.save()

        return redirect('review', id_bouquet)
