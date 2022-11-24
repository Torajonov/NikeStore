from django.db import models
from shop.models import Product

# Create your models here.
class CartProduct(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='cart_products')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.product.name)

    def get_total_price(self):
        cart_product_total_price = self.quantity * self.product.price
        return int(cart_product_total_price)

class Cart(models.Model):
    products = models.ManyToManyField(CartProduct)
    total_quantity = models.PositiveIntegerField(default=0)
    total_price = models.PositiveIntegerField(default=0)

    def add(self,product_id, qty):
        product = Product.objects.get(id=product_id)
        price = product.price * int(qty)
        self.products.create(
            product=product,
            quantity=qty,
            price=price,
            )
        self.total_quantity += int(qty)
        self.total_price += price
        self.save()
        return True

    def deleteItem(self, product_id, qty):
        product = Product.objects.get(id=product_id)
        p_id = product.id
        for item in self.products.all():
            if item.product.id == p_id:
                item.delete()
        price = product.price * int(qty)
        # self.products.remove(product)

        self.total_quantity -= qty
        self.total_price -= price
        self.save()
        return True

    def __str__(self):
        return f"{self.total_quantity}"


class OrderProduct(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='order_products')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.product.name)

class Order(models.Model):
    STATES = (
        ("Farg'ona","fergana"),
        ("Namangan","namangan"),
        ("Andijon","andijan"),
    )
    name = models.CharField('Ism-Sharifi', max_length=200)
    state = models.CharField('Viloyat', max_length=50, choices=STATES)
    address = models.CharField('Manzil', max_length=300)
    phone = models.CharField('Telefon',max_length=11 )
    products = models.ManyToManyField(OrderProduct)
    # order_sum = models.PositiveIntegerField('Narx',default=0)
    total_sum = models.PositiveIntegerField('Umumiy narx',default=0)
    payed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)