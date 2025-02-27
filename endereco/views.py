from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView
from .models import Address
from .forms import AddressForm
from django.urls import reverse_lazy
 
class AddressCreate(CreateView):
    model = Address
    form_class = AddressForm
    context_object_name = 'CreateAddressForm' #nome q o front vai acessar o formulario
    template_name = 'addressForm.html'
    success_url = reverse_lazy('endereco:list') #redericiona quando completar o formulario
    
class AddressList(ListView):
    model = Address
    template_name = 'addressList.html'
    context_object_name = 'addresses'
    
class AddressUpdate(UpdateView):
    model = Address
    form_class = AddressForm
    context_object_name = 'address'
    template_name = 'addressForm.html'
    success_url = reverse_lazy('endereco:list') 
