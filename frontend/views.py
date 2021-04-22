from django.shortcuts import render

# Create your views here.


def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')


def pendaftaran(request, *args, **kwargs):
    return render(request, 'frontend/pendaftaran.html')


def pendaftaranSukses(request, *args, **kwargs):
    return render(request, 'frontend/pendaftaransukses.html')


def strukturOrganisasi(request, *args, **kwargs):
    return render(request, 'frontend/struktur-organisasi.html')


def mainCategories(request, maincat, *args, **kwargs):
    if maincat == "home":
        return render(request, 'frontend/home.html')
    elif maincat == "about":
        return render(request, 'frontend/about.html')
    elif maincat == "blog":
        return render(request, 'frontend/blog.html')
    elif maincat == "enclass":
        return render(request, 'frontend/enclass.html')
    elif maincat == "kompeten":
        return render(request, 'frontend/kompeten.html')