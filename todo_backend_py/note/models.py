from django.db import models


class Note(models.Model):
    note = models.CharField(max_length=2000)
    title = models.CharField(max_length=300)
