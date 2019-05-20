from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from todo_backend_py.note.serializers import NoteSerializer, TitleSerializer
from todo_backend_py.note.models import Note, GetNoteResult
from todo_backend_py.common.models import Result


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class TitleView(APIView):

    def get(self, request, user, format=None):
        try:
            note = Note.objects.get(user=user)
        except Note.DoesNotExist:
            return Response([])

        serializer = TitleSerializer(note)
        return Response(serializer.data)
