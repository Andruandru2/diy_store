from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('buy/<int:id>/', views.buy_now, name='buy_now'),
    path('products/', views.all_products, name='all_products'),
    path('about/', views.about, name='about'),
]