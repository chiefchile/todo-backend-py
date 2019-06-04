from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

TITLE = "world"

NOTE = "hello"


class NoteTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user("testuser", password="testuser")
        self.client.post('/api-token-auth/', {"username": "testuser", "password": "testuser"},
                                          format='json')
        self.client.force_authenticate(user=self.user, token=self.user.auth_token)

    def create_note(self):
        return self.client.post('/note/', {"note": NOTE, "title": TITLE},
                                format='json')

    def test_get_note(self):
        create_response = self.create_note()
        url = f"/note/{create_response.data['_id']}/"

        get_response = self.client.get(url)

        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.check_note(get_response, NOTE, TITLE)

    def check_note(self, response, expected_note, expected_title):
        self.assertEqual(response.data["note"], expected_note)
        self.assertEqual(response.data["title"], expected_title)

    def test_create_note(self):
        response = self.create_note()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_note(self):
        create_response = self.create_note()
        url = f"/note/{create_response.data['_id']}/"
        updated_note = "updated note"
        updated_title = "updated title"

        response = self.client.put(url, {"note": updated_note, "title": updated_title},
                                   format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.check_note(response, updated_note, updated_title)

    def test_delete_note(self):
        create_response = self.create_note()
        url = f"/note/{create_response.data['_id']}/"

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_titles(self):
        self.create_note()

        response = self.client.get("/titles/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, TITLE)

    def test_delete_test_data(self):
        self.create_note()

        response = self.client.get("/note/deleteTestData/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)






