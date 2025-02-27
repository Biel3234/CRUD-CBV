from django.urls import path
from .views import AddressCreate, AddressList, AddressUpdate

app_name = 'endereco'

urlpatterns= [
    path('criar/', AddressCreate.as_view(), name='criar'),
    path('listar/', AddressList.as_view() ,name='list'),
    path('editar/<int:pk>', AddressUpdate.as_view(), name='atualizar')
]