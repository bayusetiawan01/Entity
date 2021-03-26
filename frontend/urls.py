from django.urls import path
from .views import index, pendaftaran

urlpatterns = [
    path('', index),
    path('pendaftaran/', pendaftaran)
]
