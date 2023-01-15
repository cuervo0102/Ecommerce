from django.urls import path
from .views import (
    home,
    checkout,
    product,
    HomeView,
    ItemDetailView,
    add_to_cart,
    remove_from_cart,
    OrderSummery
)

app_name =  'base'

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('checkout/',checkout, name='checkout'),
    path('product/<slug>',ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/',add_to_cart,name='add-to-cart'),
    path('remove-from-cart/<slug>/',remove_from_cart,name='remove-from-cart'),
    path('order-summary/',OrderSummery.as_view(),name='order-summary')

    
]