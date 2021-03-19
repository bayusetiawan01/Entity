from django.db import models
import string
import random


def generate_unique_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Event.objects.filter(code=code).count() == 0:
            break
    return code


class Event(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    judul = models.CharField(max_length=50, unique=True)
    gambar = models.CharField(max_length=50)
    deskripsi = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
