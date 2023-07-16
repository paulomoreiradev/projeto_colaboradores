from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from django.http import Http404
from app_cad_colaboradores.models import *
# Create your views here.
class colaboradores (APIView):

    def post(self,request):
        try:
            nome = request.data.get('nome')
            email = request.data.get('email')
            departamento = request.data.get('departamento')

            if(len(nome.strip())== 0):
                return Response({'response': 'O atributo nome não pode estar vazio'}, status= status.HTTP_400_BAD_REQUEST)
            if(len(email.strip())== 0): 
                return Response({'response': 'O atributo email não pode estar vazio'}, status= status.HTTP_400_BAD_REQUEST)
            if(len(departamento.strip())== 0):
                return Response({'response': 'O atributo departamento não pode estar vazio'}, status= status.HTTP_400_BAD_REQUEST)

            colaborador = Colaborador.objects.filter(nome = nome)

            if (colaborador.exists()):
                return Response({'response': 'Este colaborador já existe no banco de dados'}, status= status.HTTP_409_CONFLICT)

            try:
                colaborador = Colaborador.objects.create(nome = nome, email = email, departamento = departamento)
                colaborador.save()
                return Response({'nome':nome, 'email': email, 'departamento': departamento},status= status.HTTP_201_CREATED) 
            except:
                return Response(status= status.HTTP_500_INTERNAL_SERVER_ERROR) 
        except:
            return Response({'response': 'Confira se todos os campos estão preenchidos!'}, status= status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, id):
        try:
            colaborador = Colaborador.objects.filter(id_colaborador = id)
            serializer = ColaboradorWithIdSerializer(colaborador, many = True)
            return Response(serializer.data[0], status= status.HTTP_200_OK)
        except:
            return Response({'response': 'Colaborador não encontrado.'}, status= status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id):
        colaborador = Colaborador.objects.filter(id_colaborador = id)
        if(colaborador.exists()):
            try:
                colaborador.delete()
                return Response(status= status.HTTP_200_OK)
            except:
                return Response(status= status.HTTP_500_INTERNAL_SERVER_ERROR) 
        return Response({'response': 'Colaborador não encontrado.'}, status= status.HTTP_404_NOT_FOUND) 

        
    def put(self, request, id):
        colaborador = Colaborador.objects.filter(id_colaborador = id)
        if(colaborador.exists()):
            try:
                try:
                    nome = request.data.get('nome')
                    email = request.data.get('email')
                    departamento = request.data.get('departamento')

                    if(len(nome.strip())== 0):
                        return Response({'response': 'O atributo nome não pode estar vazio'}, status= status.HTTP_400_BAD_REQUEST)
                    if(len(email.strip())== 0): 
                        return Response({'response': 'O atributo email não pode estar vazio'}, status= status.HTTP_400_BAD_REQUEST)
                    if(len(departamento.strip())== 0):
                        return Response({'response': 'O atributo departamento não pode estar vazio'}, status= status.HTTP_400_BAD_REQUEST)
                    
                    colaborador.update(nome = nome, email = email, departamento = departamento)
                    return Response({'nome':nome, 'email': email, 'departamento': departamento},status= status.HTTP_200_OK)


                except:
                    return Response({'response': 'Confira se todos os campos estão preenchidos!'}, status= status.HTTP_400_BAD_REQUEST)                
                
            except:
                return Response(status= status.HTTP_500_INTERNAL_SERVER_ERROR) 
        return Response({'response': 'Colaborador não encontrado.'}, status= status.HTTP_404_NOT_FOUND)

        
    
class colaboradoresGetAll (APIView):
    def get(self, request):
        colaborador = Colaborador.objects.all()
        serializer = ColaboradorSerializer(colaborador, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    

        
        
