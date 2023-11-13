from django.urls import path
from .views import carts , view_cart, add_to_cart, remove_from_cart, checkout
from .views import process_payment


app_name = 'cart' 

urlpatterns = [
    path('carts/', carts, name='carts'),
    path('carts/', view_cart, name='view_cart'),
    # path('view/', view_cart, name='view_cart'),
    # path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('add_to_cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('process-payment/', process_payment, name='process_payment'),

]
