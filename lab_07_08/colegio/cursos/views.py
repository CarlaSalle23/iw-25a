from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Silabo
from .serializers import SilaboSerializer
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class SilaboList(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        silabos = Silabo.objects.all()
        serializer = SilaboSerializer(silabos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SilaboSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SilaboDetail(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        silabo = get_object_or_404(Silabo, pk=pk)
        serializer = SilaboSerializer(silabo)
        return Response(serializer.data)

    def put(self, request, pk):
        silabo = get_object_or_404(Silabo, pk=pk)
        serializer = SilaboSerializer(silabo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        silabo = get_object_or_404(Silabo, pk=pk)
        silabo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
