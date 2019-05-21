from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import viewsets, mixins, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from todo_backend_py.note.serializers import NoteSerializer, TitleSerializer
from todo_backend_py.note.models import Note, User


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


# Delete all notes of testuser -- used in end to end testing
def deleteTestData(request):
    Note.objects.filter(user="testuser").delete()
    return HttpResponse(status=status.HTTP_200_OK)


class TitleView(APIView):

    def get(self, request, user, format=None):
        try:
            note = Note.objects.filter(user=user)
        except Note.DoesNotExist:
            return Response([])

        serializer = TitleSerializer(note, many=True)
        return Response(serializer.data)


class LoginView(APIView):

    def post(self, request, format=None):
        try:
            user = User.objects.get(
                username=request.data["username"], password=request.data["password"])
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_200_OK)
