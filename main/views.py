# from django.shortcuts import render
# from django.http import HttpResponse
# def main(request):
# return HttpResponse("You're on main")

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Bouquet


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


class Constructor(DetailView):
    pass