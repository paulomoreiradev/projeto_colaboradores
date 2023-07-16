from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    # path('', views.home, name = 'home'),
    # path('colaboradores/', views.colaboradores, name = 'listagem_colaboradores'),
    # path('api/', include('api.urls', namespace = 'api'))
    path('colaboradores/', colaboradores.as_view(), name = 'colaboradores'),
    path('colaboradores/<int:id>', colaboradores.as_view(), name = 'colaboradorWithId'),
    path('colaboradores/getAll', colaboradoresGetAll.as_view(), name = 'listagem_de_colaboradores')
]