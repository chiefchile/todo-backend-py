from builtins import classmethod

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from todo_backend_py.note.models import Note


class NoteTests(APITestCase):

    # @classmethod
    def setUp(self):
        self.user = User.objects.create_user("testuser", password="testuser")
        self.client.post('/api-token-auth/', {"username": "testuser", "password": "testuser"},
                                          format='json')

    def create_note(self):
        self.client.force_authenticate(user=self.user, token=self.user.auth_token)
        return self.client.post('/note/', {"note": "note", "title": "title"},
                                    format='json')

    def test_get_note(self):
        response = self.create_note()
        self.client.force_authenticate(user=self.user, token=self.user.auth_token)
        url = f"/note/{response.data['_id']}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_note(self):
        self.client.force_authenticate(user=self.user, token=self.user.auth_token)
        response = self.create_note()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
