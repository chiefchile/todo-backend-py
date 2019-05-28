import logging

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import viewsets, mixins, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin

from todo_backend_py.note.serializers import NoteSerializer, TitleSerializer
from todo_backend_py.note.models import Note, User
from todo_backend_py.note.permissions import IsUser


logger = logging.getLogger(__name__)


class NoteViewSet(viewsets.GenericViewSet,
                  CreateModelMixin,
                  UpdateModelMixin,
                  DestroyModelMixin,
                  RetrieveModelMixin):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticated, IsUser,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Delete all notes of testuser -- used in end to end testing
def delete_test_data(request):
    Note.objects.filter(user="testuser").delete()
    return HttpResponse(status=status.HTTP_200_OK)


class TitleView(APIView):
    permission_classes = (permissions.IsAuthenticated, IsUser,)

    def get(self, request, format=None):
        try:
            note = Note.objects.filter(user__username=request.user).order_by("title")
        except Note.DoesNotExist:
            return Response([])

        serializer = TitleSerializer(note, many=True)
        return Response(serializer.data)
