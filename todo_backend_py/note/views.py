from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from todo_backend_py.note.serializers import NoteSerializer
from todo_backend_py.note.models import Note, GetNoteResult
from todo_backend_py.common.models import Result


class NoteView(APIView):
	
	def get(self, request, pk, format=None):
		note = Note.objects.get(pk=pk)
		serializer = NoteSerializer(note)
		result = GetNoteResult(code=0, msg="Success", note=serializer.data)
		return Response(vars(result))
