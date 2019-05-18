from rest_framework import serializers
from todo_backend_py.note.models import Note


class NoteSerializer(serializers.ModelSerializer):
	_id = serializers.CharField(source='id')
	
	class Meta:
		model = Note
		fields = ('_id', 'title', 'note', 'user')
