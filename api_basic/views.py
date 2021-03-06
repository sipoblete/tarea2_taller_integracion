# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from rest_framework.parsers import JSONParser
# from .models import Hamburguesa
# from .serializers import HamburguesaSerializer
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView



from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import HamburguesaSerializer, IngredienteSerializer
from .models import Hamburguesa
from .models import Ingrediente
# Create your views here.


class HamburguesaAPIView(APIView):
    def get(self, request):
        hamburguesas = Hamburguesa.objects.all()
        serializer = HamburguesaSerializer(hamburguesas, many=True)
        return Response(serializer.data, status=)
    
    def post(self, request):
        serializer = HamburguesaSerializer(data=request.data)
        

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class HamburguesaDetails(APIView):
    def get_object(self,id):
        try:
            return Hamburguesa.objects.get(id=id)
        except Hamburguesa.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        hamburguesa = self.get_object(id)
        serializer = HamburguesaSerializer(hamburguesa)
        return Response(serializer.data)


    def patch(self, request, id):
        hamburguesa = self.get_object(id)
        serializer = HamburguesaSerializer(hamburguesa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        hamburguesa = self.get_object(id)
        hamburguesa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






class IngredienteAPIView(APIView):
    def get(self, request):
        ingredientes = Ingrediente.objects.all()
        serializer = IngredienteSerializer(ingredientes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = IngredienteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class IngredienteDetails(APIView):
    def get_object(self,id):
        try:
            return Ingrediente.objects.get(id=id)
        except Ingrediente.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        ingrediente = self.get_object(id)
        serializer = IngredienteSerializer(ingrediente)
        return Response(serializer.data)



    def delete(self, request, id):
        ingrediente = self.get_object(id)
        ingrediente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class HamburguesaIngrediente(APIView):
    def get_hamburguesa(self,id):
        try:
            return Hamburguesa.objects.get(id=id)
        except Hamburguesa.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def get_ingrediente(self,id):
        try:
            return Ingrediente.objects.get(id=id)
        except Ingrediente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self,request,id, iid):
        hamburguesa = self.get_hamburguesa(id)
        ingrediente = self.get_ingrediente(id=iid)
        hamburguesa.ingredientes.add(ingrediente)
        return Response(status=status.HTTP_201_CREATED)

    def delete(self,request,id, iid):
        hamburguesa = self.get_hamburguesa(id)
        ingrediente = self.get_ingrediente(iid)
        try:
            hamburguesa.ingredientes.remove(ingrediente)
            return Response(status=status.HTTP_200_OK)
        except Ingrediente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)