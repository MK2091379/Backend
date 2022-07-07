from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NoteBasicSerializer,NoteFileSerializer,NoteDetailsSerializer,NoteBasic2Serializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import Files, Note
from rest_framework.decorators import action



from rest_framework.pagination import PageNumberPagination





class AddFileView(APIView):
    serializer_class=NoteBasic2Serializer
    def post(self, request, *args, **kwargs):
        notepost = Note.objects.create(user_id=request.user.id)
        note_serializer = NoteBasicSerializer(notepost,data=self.request.data)
        note_serializer.is_valid(raise_exception=True)
        _note = note_serializer.save()
        for file in self.request.FILES.getlist('files'):
                note_file = NoteFileSerializer(
                    data={
                        'file': file,
                        'note': _note.id
                        
                    }
                )
                note_file.is_valid(raise_exception=True)
                note_file.save()
        return Response(status=status.HTTP_200_OK)
        

        


class FileQuery(ModelViewSet):
    serializer_class=NoteDetailsSerializer
    queryset = Note.objects.all()
    
    pagination_class=PageNumberPagination
    @action(detail=False,methods=['GET'])
    def show_my_notes(self,request):
        paginator=PageNumberPagination()
        paginator.page_size=4
        queryset=paginator.paginate_queryset(Note.objects.filter(user_id=request.user.id),request)
        serializer=NoteDetailsSerializer(queryset,many=True)
        return paginator.get_paginated_response(serializer.data)
    
    @action(detail=False, method=['DELETE'])
    def delete_file(self,request,id):
        getfile=get_object_or_404(Files,id=id,note__user_id=request.user.id)
        getfile.delete()
        return Response(status=status.HTTP_200_OK) 
    
    @action(detail=False, method=['DELETE'])
    def delete_note(self,request,id):
        getnote=get_object_or_404(Note,id=id,user_id=request.user.id)
        getnote.delete()
        return Response(status=status.HTTP_200_OK) 
    
    @action(detail=False , methods=['PATCH'])
    def update_note(self,request,id):
        getnote=get_object_or_404(Note,id=id,user_id=request.user.id)
        serializer=NoteDetailsSerializer(getnote,data=request.data)
        serializer.is_valid(raise_exception=True)
        _note=serializer.save()
        for file in self.request.FILES.getlist('files'):
                note_file = NoteFileSerializer(
                    data={
                        'file': file,
                        'note': _note.id
                        
                    }
                )
                note_file.is_valid(raise_exception=True)
                note_file.save()
        return Response(serializer.data,status=status.HTTP_200_OK) 
    
  

    
        
        
        