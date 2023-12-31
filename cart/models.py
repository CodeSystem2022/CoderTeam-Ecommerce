# models.py
# from django.db import models
# from django.contrib.auth.models import User

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)

# class Cart(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product, through='CartItem')

# class CartItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

# cart/models.py
from django.db import models
from django.contrib.auth.models import User
from item.models import Item

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, through='CartItem')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)