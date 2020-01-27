from django.shortcuts import render
from .models import Register
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer,RegisterCreate
from rest_framework import generics
from rest_framework.generics import DestroyAPIView,ListAPIView,UpdateAPIView,CreateAPIView,RetrieveAPIView
# Create your views here.
class RegisterSearchView(APIView):
    def get(self,request,format=None):
        qs=Register.objects.all()
        serializer=RegisterSerializer(qs,many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        qs=Register.objects.all()
        serializer=RegisterSerializer(qs,many=True)
        return Response(serializer.data)
class RegisterList(generics.ListAPIView):
    queryset        =Register.objects.all()
    serializer_class=RegisterSerializer
    def get_queryset(self):
        qs=Register.objects.all()
        query=self.request.GET.get('q')
        if query is not None:
            qs=qs.filter(desc__icontains=query)
        return qs
class RegisterCreate(generics.CreateAPIView):
    queryset        =Register.objects.all()
    serializer_class=RegisterCreate
class RegisterRetrieve(generics.RetrieveAPIView):
    queryset        =Register.objects.all()
    serializer_class=RegisterSerializer
class RegisterUpdate(generics.UpdateAPIView):
    queryset        =Register.objects.all()
    serializer_class=RegisterSerializer
class RegisterDestroy(generics.DestroyAPIView):
    queryset        =Register.objects.all()
    serializer_class=RegisterSerializer


