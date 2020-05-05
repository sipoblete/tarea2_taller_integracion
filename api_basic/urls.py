from django.urls import path
from .views import HamburguesaAPIView, IngredienteAPIView, HamburguesaDetails, IngredienteDetails, HamburguesaIngrediente

urlpatterns = [
    path('ingrediente', IngredienteAPIView.as_view()),
    path('hamburguesa', HamburguesaAPIView.as_view()),
    path('hamburguesa/<int:id>', HamburguesaDetails.as_view()),
    path('ingrediente/<int:id>', IngredienteDetails.as_view()),
    path('hamburguesa/<int:id>/ingrediente/<int:iid>', HamburguesaIngrediente.as_view()),
    
    
]
    
