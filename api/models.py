from django.db import models
import string
import random


class Event(models.Model):
    judul = models.CharField(max_length=50, unique=True)
    gambar = models.CharField(max_length=50, blank=True, null=True)
    deskripsi = models.CharField(max_length=1024, blank=True, null=True)
    dd_date = models.DateTimeField(auto_now_add=True)


class Pendaftaran(models.Model):
    nama = models.CharField(max_length=50)
    npm = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    motivasi = models.TextField(blank=True, null=True)
    menjadi_pengurus = models.BooleanField(null=False, default=1)
    minat1 = models.CharField(max_length=50, blank=True, null=True)
    minat2 = models.CharField(max_length=50, blank=True, null=True)
    hari = models.CharField(max_length=50, blank=True, null=True)
    bahasa = models.CharField(max_length=50, blank=True, null=True)
    harapan = models.TextField(blank=True, null=True)
    dd_date = models.DateTimeField(auto_now_add=True)
