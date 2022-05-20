from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import NoteSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import Note

class FileView(ModelViewSet):

  serializer_class =NoteSerializers
  queryset=Note.objects.all()
  parser_classes = (MultiPartParser, FormParser)
  action(detail=False , methods=['POST'])
  def note_view(self, request):
    file = list( request.FILES.values())
    file_serializer = NoteSerializers(data={"file":file})
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)