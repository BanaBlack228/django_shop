from itertools import product

from django.shortcuts import render
from decimal import Decimal

from shop.models import Product
from .models import CartUser, CartItem
from shopproject.settings import CART_SESSION_ID


class Cart:
    """
    Класс корзины для анонимного пользователя(неавторизованного)
    """
    def __init__(self, request):
        self.session = request.session
        self.user = request.user
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def save(self):
        self.session.modified = True

    def copy(self):
        return self.cart.copy()


    def add(self, product, quantity = 1, override_quantity=False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }

        if override_quantity:
            self.cart[product_id][quantity] = quantity
        else:
            self.cart[product_id][quantity] += quantity


        self.save()

    def remove(self,product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in  self.cart.values())

    def clear(self):
        self.cart.clear()
        self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item