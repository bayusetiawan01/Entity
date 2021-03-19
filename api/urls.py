from django.urls import path
from .views import EventView

urlpatterns = [
    path('home', EventView.as_view()),
]
