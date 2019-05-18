from django.db import models

class Result:
	
	def __init__(self, code, msg):
		self.code = code
		self.msg = msg
