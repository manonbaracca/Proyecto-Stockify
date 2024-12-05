from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index (request):
    return render (request, 'dashboard/index.html')

@login_required

def staff (request):
    return render (request, 'dashboard/staff.html')

@login_required
def producto (request):
    return render (request, 'dashboard/producto.html')

@login_required
def pedido (request):
    return render (request, 'dashboard/pedido.html')