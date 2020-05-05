from rest_framework import serializers
from .models import Hamburguesa
from .models import Ingrediente


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['nombre', 'descripcion']

    def get_queryset(self):
            return Ingrediente.objects.all()

class HamburguesaSerializer(serializers.ModelSerializer):
    ingredientes = IngredienteSerializer(read_only = True, many=True)
    class Meta:
        model = Hamburguesa
        fields = ['id','nombre', 'precio', 'descripcion', 'imagen', 'ingredientes']
    
    def get_queryset(self):
        return Hamburguesa.objects.all()



