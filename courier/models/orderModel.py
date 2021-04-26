from django.db import models
from .userModel import User


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_from = models.IntegerField(blank=True, null=True)
    merchant = models.ForeignKey(User, on_delete=models.DO_NOTHING,)
    product_type = models.CharField(max_length=30, blank=True, null=True)
    invoice_id = models.CharField(max_length=300, blank=True, null=True)
    location = models.CharField(max_length=25, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)