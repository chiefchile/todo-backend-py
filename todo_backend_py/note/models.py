from django.db import models

from todo_backend_py.common.models import Result


class Note(models.Model):
	note = models.CharField(max_length=2000)
	title = models.CharField(max_length=300)
	user = models.CharField(max_length=50, default=None)
	
	def __str__(self):
		return self.title
		
		
class GetNoteResult(Result):
	
	def __init__(self, code, msg, note):
		self.code = code
		self.msg = msg
		self.note = note
