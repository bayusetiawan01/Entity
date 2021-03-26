from django.shortcuts import render
from rest_framework import generics
from .serializers import EventSerializer, PendaftaranSerializer, CreatePendaftaranSerializer
from .models import Event, Pendaftaran
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class EventView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class PendaftaranView(generics.CreateAPIView):
    queryset = Pendaftaran.objects.all()
    serializer_class = PendaftaranSerializer


class CreatePendaftaranView(APIView):
    serializer_class = CreatePendaftaranSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            nama = serializer.data.nama
            npm = serializer.data.npm
            email = serializer.data.email
            motivasi = serializer.data.motivasi
            menjadi_pengurus = serializer.data.manjadi_pengurus
            minat = serializer.data.minat
            hari = serializer.data.hari
            bahasa = serializer.data.bahasa
            harapan = serializer.data.harapan
            pendaftaran = Pendaftaran(nama=nama, npm=npm, email=email, motivasi=motivasi, menjadi_pengurus=menjadi_pengurus,
                                      minat=minat, hari=hari, bahasa=bahasa, harapan=harapan)
            pendaftaran.save()

            return Response(PendaftaranSerializer(pendaftaran).data, status=status.HTTP_200_OK)
