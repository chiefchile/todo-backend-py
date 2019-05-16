from django.shortcuts import render
from rest_framework import viewsets
from todo_backend_py.note.serializers import NoteSerializer
from todo_backend_py.note.models import Note


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
