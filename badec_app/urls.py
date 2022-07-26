from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  
    path('', views.home, name='home'),
    path('reservationsalle/', views.reservationsalle, name='reservationsalle'),
    path('paiement/', views.paiement, name='paiement')

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)