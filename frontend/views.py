from django.shortcuts import render

# Create your views here.


def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')


def pendaftaran(request, *args, **kwargs):
    return render(request, 'frontend/pendaftaran.html')


def pendaftaranSukses(request, *args, **kwargs):
    return render(request, 'frontend/pendaftaransukses.html')
