from django.db import models
from rest_framework import serializers

class Colaborador(models.Model):
    id_colaborador = models.AutoField(primary_key = True)
    nome = models.TextField(max_length=255)
    email = models.EmailField(max_length=255)
    departamento = models.TextField(max_length=255)

class ColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaborador
        fields = ['nome', 'email', 'departamento']

class ColaboradorWithIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaborador
        fields = '__all__'

