from dataclasses import field
from pyexpat import model
from .models import Note,Files
from rest_framework import serializers




class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields="__all__"

class NoteSingleFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = ['file']
        
class NoteDetailsSerializer(serializers.ModelSerializer):
    carimage_set=NoteSingleFileSerializer(many=True)
    class Meta:
        model = Note
        fields = ['title','text','files_set']

class NoteFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = "__all__"
