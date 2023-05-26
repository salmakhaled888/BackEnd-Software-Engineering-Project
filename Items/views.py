from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from Items.serializer import ItemSerializer
from .models import Item

# Create your views here.
class ItemViewset(viewsets.ViewSet):
    def list(self, request:Request):
        queryset = Item.objects.all()
        serializer = ItemSerializer(instance=queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request:Request, pk=None):
        post = get_object_or_404(Item, pk=pk)
        serializer = ItemSerializer(instance=post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)