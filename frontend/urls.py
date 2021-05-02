from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('pendaftaran/', pendaftaran),
    path('pendaftaran-berhasil/', pendaftaranSukses),
    path('<str:maincat>/', mainCategories),
    path('about/struktur-organisasi/', strukturOrganisasi),
    path('enclass/<str:subcat>/', subCategories),
]
