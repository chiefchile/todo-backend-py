from django.db import models

from todo_backend_py.common.models import Result


class Note(models.Model):
    note = models.CharField(max_length=2000)
    title = models.CharField(max_length=300)
    user = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=50, default=None)
    password = models.CharField(max_length=50, default=None)
