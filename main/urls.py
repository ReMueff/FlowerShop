from django.conf.urls.static import static
from django.urls import path

from django.conf import settings
from . import views

urlpatterns = [
    # static('main' + settings.STATIC_URL),
    # static('main' + settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),

    path('main/', views.MainPage.as_view(), name='main'),
    path('main/<int:pk>/review/', views.Reviewer.as_view(), name='review'),
    path(r'main/<int:pk>', views.CheckDescription.as_view(), name='check_description')

    # path('main/<int:pk>', views.CreateBouquet.as_view(), name='create')
]

urlpatterns += static('main' + settings.STATIC_URL)
urlpatterns += static('main' + settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
