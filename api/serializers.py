from rest_framework import serializers
from .models import Event, Pendaftaran


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'judul', 'gambar', 'deskripsi', 'dd_date')


class PendaftaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pendaftaran
        fields = ('id', 'nama', 'npm', 'email', 'motivasi', 'menjadi_pengurus',
                  'minat', 'hari', 'bahasa', 'harapan', 'dd_date')


class CreatePendaftaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pendaftaran
        fields = ('nama', 'npm', 'email', 'motivasi', 'menjadi_pengurus',
                  'minat', 'hari', 'bahasa', 'harapan')
