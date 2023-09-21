from django.db import models
from internal.models import Order, Package_Category, Payment
from django.contrib.auth.models import User

# Create your models here.
class ProductStock(models.Model):
    product_name = models.CharField('Product Name', max_length=250)
    quantity = models.IntegerField()

class SaleHistory(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    package = models.ForeignKey(Package_Category, on_delete=models.CASCADE)

class PaymentHistory(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    customer = models.ForeignKey(User, on_delete= models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)