import os
from io import BytesIO
from uuid import uuid4

from django.shortcuts import redirect
from django.views.generic import ListView, FormView, DetailView
from PIL import Image
from .forms import SelectBouquet, ChangeBouquetInfo
from .models import Bouquet, BouquetFlowers, Flower
from django.core.files.images import ImageFile


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

    def post(self, request, *args, **kwargs):
        new_bouquet = Bouquet.objects.create(
            name=f"bouquet_{uuid4()}",
            description=f"description_{uuid4()}"
        )

        return redirect('review', new_bouquet.id)


class Reviewer(FormView):
    template_name = "review.html"
    model = BouquetFlowers
    context_object_name = 'bouquet'
    form_class = SelectBouquet
    positions_coord = {1: (0, 0), 2: (500, 0), 3: (1000, 0),
                       4: (0, 500), 5: (500, 500), 6: (1000, 500),
                       7: (0, 1000), 8: (500, 1000), 9: (1000, 1000)}

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
        context['bouquet'] = Bouquet.objects.get(id=self.kwargs.get('pk'))
        context['position_form'] = SelectBouquet()
        context['bouquet_form'] = ChangeBouquetInfo(
            initial={
                'set_name': context['bouquet'].name,
                'set_description': context['bouquet'].description
            }
        )
        return context

    def post(self, request, *args, **kwargs):
        id_bouquet = self.kwargs.get('pk')
        current_bouquet = Bouquet.objects.get(id=id_bouquet)
        if request.POST.get('set_name'):
            current_bouquet.name = request.POST.get('set_name')
            current_bouquet.description = request.POST.get('set_description')
            current_bouquet.save()
            return redirect('review', id_bouquet)

        position = int(request.POST.get('sel_position'))
        flower_id = int(request.POST.get('sel_flower'))
        amount = int(request.POST.get('sel_amount'))
        instance, created = BouquetFlowers.objects.update_or_create(
            bouquet_id=id_bouquet, position=position, flower_id=flower_id
        )

        instance.amount = amount
        instance.refresh_from_db()
        instance.save()
        self.get_context_data()
        self.set_collage()

        return redirect('review', id_bouquet)

    def set_collage(self):
        collage = Image.new("RGBA", (1500, 1500), color=(255, 255, 255, 255))
        lst = [100, 200, 300, 400, 500, 600, 700, 800, 900]
        context = self.get_context_data()
        bouquet = context['bouquet']
        bouquet.collage.flush()
        for key in context['positions']:
            file = "media/" + str(context['positions'][key])
            photo = Image.open(file).convert("RGBA")
            photo = photo.resize((500, 500))
            collage.paste(photo, self.positions_coord[int(key)])
            photo.close()
        new_image_url = f"{uuid4()}.png"
        collage.save("media/bouquet/" + new_image_url)
        with open("media/bouquet/" + new_image_url, mode="rb") as file:
            bouquet.collage = ImageFile(file, name=new_image_url)
            # if os.path.isfile("media/bouquet/" + old_preview.flush):
            #     os.remove("media/bouquet/" + old_preview)
            bouquet.save()

        collage.show()


class CheckDescription(DetailView):
    model = Bouquet
    template_name = 'bouquetdescription.html'
    context_object_name = 'bouquet'

    def get_queryset(self):
        return Bouquet.objects.filter(id=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bouquet'] = Bouquet.objects.get(id=self.kwargs.get('pk'))
        description = context['bouquet'].description
        name = context['bouquet'].name
        collage = context['bouquet'].collage
        return context


    


# class CreateBouquet(FormView):
#     template_name = "review.html"
#     model = BouquetFlowers
#     context_object_name = 'bouquet'
#     form_class = SelectBouquet
#
#     def post(self, request, *args, **kwargs):
#         id_bouquet = self.kwargs.get('pk')
#         position = int(request.POST.get('sel_position'))
#         flower_id = int(request.POST.get('sel_flower'))
#         amount = int(request.POST.get('sel_amount'))
#         instance, created = BouquetFlowers.objects.update_or_create(
#             bouquet_id=id_bouquet, position=position, flower_id=flower_id
#         )
#
#         instance.amount = amount
#         instance.save()
#         instance.refresh_from_db()
#         self.get_context_data()
#         self.set_collage()
#
#         return redirect('review', id_bouquet)
