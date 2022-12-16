from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from vehicles.serializers import VehicleSerializer
from vehicles.models import Vehicles



class VehiclesView(APIView):
    def get(self,request,*args,**kw):
        qs=Vehicles.objects.all()
        sz=VehicleSerializer(qs,many=True) #de serialization
        return Response(data=sz.data)
    def post(self,request,*args,**kw):
       serializer=VehicleSerializer(data=request.data)
       if serializer.is_valid():
        Vehicles.objects.create(**serializer.validated_data)
        return Response(data=serializer.data)
       else:
        return Response(data=serializer.errors)

#localhost:8000/vehicles/{id}
class VehicleDetailsView(APIView):

    def get(self,request,*args,**kw):
        id=kw.get("id")
        qs=Vehicles.objects.get(id=id)
        serializer=VehicleSerializer(qs)
        return Response(data=serializer.data)
    def delete(self,request,*args,**kw):
        id=kw.get("id")
        Vehicles.objects.filter(id=id).delete()
        return Response(data="deleted")

    def put(self,request,*args,**kw):
        id=kw.get("id")
        serializer=VehicleSerializer(data=request.data)
        if serializer.is_valid():
            Vehicles.objects.filter(id=id).update(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
       
