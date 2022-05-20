from .models import Note,Files
from rest_framework import serializers




class NoteBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields="__all__"

class NoteSingleFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = ['file']
        
class NoteDetailsSerializer(serializers.ModelSerializer):
    files_set=NoteSingleFileSerializer(many=True)
    class Meta:
        model = Note
        fields = ['id','user','title','text','files_set']

class NoteFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = "__all__"
