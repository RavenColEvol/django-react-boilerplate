from django.shortcuts import render
from rest_framework import generics
from ponynotes.serializers import NoteSerializer
from ponynotes.models import Note

class NoteView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer