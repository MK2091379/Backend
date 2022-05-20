from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NoteBasicSerializer,NoteFileSerializer,NoteDetailsSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import Note

class AddFileView(APIView):
    def post(self, request, *args, **kwargs):
        
        notepost = Note.objects.create(user_id=request.user.id)
        note_serializer = NoteBasicSerializer(notepost,data=self.request.data)
        if note_serializer.is_valid():
            _note = note_serializer.save()
            for file in self.request.FILES.getlist('files'):
                note_file = NoteFileSerializer(
                    data={
                        'file': file,
                        'note': _note.id
                        
                    }
                )
                if note_file.is_valid():
                    note_file.save()
                else:
                    return Response(note_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(note_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(NoteDetailsSerializer(_note).data, status=status.HTTP_201_CREATED)