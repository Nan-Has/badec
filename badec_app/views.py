from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'main.html')


def reservation(request):
    return render(request,'reservationsalle.html')
