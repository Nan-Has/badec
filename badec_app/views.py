from click import style
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'style/accueil.html')


def reservationsalle(request):
    return render(request,'style/reservationsalle.html')


def paiement(request):
    return render(request, 'style/paiement.html')