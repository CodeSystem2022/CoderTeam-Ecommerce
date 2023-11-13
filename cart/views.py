from django.shortcuts import render, redirect, get_object_or_404
from item.models import Item
from .models import Cart, CartItem 
#from .models import Cart, Product, CartItem

# def view_cart(request):
#     cart = get_object_or_404(Cart, user=request.user)
#     cart_items = cart.cartitem_set.all()
#     total_price = sum(item.product.price * item.quantity for item in cart_items)
#     return render(request, 'cart/view_cart.html', {'cart_items': cart_items, 'total_price': total_price})

# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
#     cart, created = Cart.objects.get_or_create(user=request.user)
#     cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
#     if not created:
#         cart_item.quantity += 1
#         cart_item.save()
#     return render(request, 'cart/add_to_cart.html', {'product': product})

def carts(request):
    # Obtener el carrito del usuario actual o crear uno nuevo si no existe
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Obtener todos los elementos en el carrito actual
    cart_items = CartItem.objects.filter(cart=cart)

    # Calcular el total del carrito sumando el precio de cada artículo multiplicado por la cantidad
    total = sum(item.item.price * item.quantity for item in cart_items)

    return render(request, 'cart/carts.html', {
        'cart_items': cart_items,
        'total': total,
    })

def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()
    total_items = sum(item.quantity for item in cart_items)
    return render(request, 'cart/carts.html', {'cart_items': cart_items, 'total_items': total_items})

def add_to_cart(request, item_id):
    cart = get_or_create_cart(request)
    item = get_object_or_404(Item, id=item_id)

    # Verificar si el artículo ya está en el carrito
    cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)

    if not created:
        # Si ya existe, incrementar la cantidad en lugar de crear un nuevo elemento
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart:carts')

def remove_from_cart(request, item_id):
    # Obtén el item
    item = get_object_or_404(Item, pk=item_id)

    # Obtén el carrito del usuario actual
    cart = Cart.objects.get(user=request.user)

    # Obtén el objeto CartItem asociado al item y carrito
    cart_item = get_object_or_404(CartItem, cart=cart, item=item)

    # Decrementa la cantidad en 1; si llega a 0, elimina el CartItem
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart:carts')

def checkout(request):
    # Obtén el carrito del usuario actual
    cart = Cart.objects.get(user=request.user)

    # Puedes realizar acciones adicionales aquí, como procesar el pago, generar una orden, etc.

    # Limpia el carrito después del checkout
    cart.cartitem_set.all().delete()

    return render(request, 'cart/checkout.html')