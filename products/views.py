from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Product
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer
from datetime import date
# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def hello(request):
    return JsonResponse({"message": "Hello, world!"})

def colado(request, precio=None, activo=None):
    
    products = list(Product.objects.all().values())
    
    product = products[0]
    
    print(products)
    
    print(precio)
    
    print(activo)

    objeto = {
        'producto': 'Camiseta 212',
        'precio': 129,
        'fecha': date.today()
    }

    # regresar una vista visual
    return render(request,'products/index.html', objeto)

    # regresar un json plano    
    # return JsonResponse(product, safe=False)
    
    # return HttpResponse("Hola mundo desde colado.")

def detalleProducto(request):

    product = Product.objects.filter(id=100).first()

    print('product')
    print(product)

    return render(request, 'products/detalle.html', {'product': product})

def status(request):
    return JsonResponse({
        "status": "OK",
        "service": "Products",
        "version": "1.0",
    })