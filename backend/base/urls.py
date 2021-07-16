from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes, name=""),
    path('products/', views.getProducts, name="products"),
]
