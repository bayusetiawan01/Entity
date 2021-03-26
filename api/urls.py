from django.urls import path
from .views import EventView, PendaftaranView, CreatePendaftaranView

urlpatterns = [
    path('home', EventView.as_view()),
    path('pendaftaran', PendaftaranView.as_view()),
    path('create-pendaftaran', CreatePendaftaranView.as_view()),
]
