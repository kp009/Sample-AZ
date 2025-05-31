from django.urls import path
from .views import home
from . import views
from .views import ProductListCreateView


urlpatterns = [
    path('', home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('api/products/', ProductListCreateView.as_view(), name='product-list-create'),

]
