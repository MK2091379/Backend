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
        fields = ['id','title','text','files_set']
        read_only=['id']

class NoteFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = "__all__"


class NoteBasic2Serializer(serializers.ModelSerializer):
    note=NoteBasicSerializer()
    class Meta:
        model=Files
        fields=['file','note']

