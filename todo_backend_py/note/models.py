from django.db import models

from todo_backend_py.common.models import Result


class Note(models.Model):
    note = models.CharField(max_length=2000, blank=True, default='')
    title = models.CharField(max_length=300)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=50, default=None)
    password = models.CharField(max_length=50, default=None)
