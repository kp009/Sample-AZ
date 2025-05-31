from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    #return HttpResponse("Hello from the Core App!")
    return render(request, "index.html")

from .models import Product

def product_list(request):
    products = [
        {
            'name': 'Laptop',
            'price': '999.99',
            'description': 'A high-performance laptop suitable for all your work and gaming needs.'
        },
        {
            'name': 'Keyboard',
            'price': '49.99',
            'description': 'A mechanical keyboard with RGB lighting and responsive keys.'
        }
    ]
    return render(request, 'product_list.html', {'products': products})

from .serializers import ProductSerializer
from rest_framework import generics


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer