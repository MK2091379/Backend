from .models import Note
from rest_framework import serializers




class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        Model=Note
        fields=['title','text','file'] 