from django.conf.urls.static import static
from django.urls import path

from django.conf import settings
from . import views

urlpatterns = [
    path('main/', views.MainPage.as_view(), name='main'),
    path('main/<int:pk>', views.Reviewer.as_view(), name='review')
]


urlpatterns += static('main' + settings.STATIC_URL)
urlpatterns += static('main' + settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)