from django.urls import path
from .views import index, pendaftaran, pendaftaranSukses

urlpatterns = [
    path('', index),
    path('pendaftaran/', pendaftaran),
    path('pendaftaran-berhasil/', pendaftaranSukses)
]
