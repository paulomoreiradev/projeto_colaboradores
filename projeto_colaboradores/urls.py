from django.urls import path, include
from app_cad_colaboradores import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('colaboradores/paineldecontrole', views.listaColaboradores, name = 'painel_controle'),
    path('colaboradores/', views.colaboradores, name = 'listagem_colaboradores'),
    path('delete/<int:id>',views.deletar, name = 'deletar'),
    path('editar/<int:id>',views.editar, name = 'editar'),
    path('api/', include('api.urls', namespace = 'api'))
]
