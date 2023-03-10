from django.db import models


class Order(models.Model):
    total = models.DecimalField(decimal_places=3, max_digits=20)
    status = models.CharField(max_length=100)


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.DecimalField(decimal_places=3, max_digits=20)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=None)
    quantity = models.IntegerField()
