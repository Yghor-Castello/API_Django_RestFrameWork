from django.urls import path

from .views import CursoAPIView, CursosAPIView, AvaliacaoAPIView, AvaliacoesAPIView

#Rotas do Django (Endpoints)
urlpatterns = [
    #Rotas criadas para get, put e delete
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    #Rotas criadas com complemento para os metodos "get, put e delete"
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
    path('avaliacoes/<int:pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
    
    

]
