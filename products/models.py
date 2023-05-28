from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class CartItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Food(models.Model):
    title = models.CharField(max_length=50, blank=False, default='')
    price = models.CharField(max_length=20, blank=False)


class Order(models.Model):
    id = models.CharField(max_length=50, blank=False, default='', primary_key=True)
    title = models.CharField(max_length=100, blank=False)