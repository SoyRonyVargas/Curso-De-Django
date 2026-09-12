from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Product
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer
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

    # regresar una vista visual
    return render(request,'products/index.html', product)

    # regresar un json plano    
    # return JsonResponse(product, safe=False)
    
    # return HttpResponse("Hola mundo desde colado.")

def status(request):
    return JsonResponse({
        "status": "OK",
        "service": "Products",
        "version": "1.0",
    })