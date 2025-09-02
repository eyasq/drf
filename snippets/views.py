from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.shortcuts import get_object_or_404

# Create your views here.


class SnippetList(APIView):
    def get(self,request):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request):
        serializer=SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SnippetDetail(APIView):

    def get(self,request, id):
        snippet = get_object_or_404(Snippet, id=id)
        data = SnippetSerializer(snippet)
        return Response(data.data, status=status.HTTP_200_OK)
    def put(self,request,id):
        snippet = get_object_or_404(Snippet, id=id)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        snippet = get_object_or_404(Snippet, id=id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



