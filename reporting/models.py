from django.db import models
from internal.models import Payment, AbstractUserModel
from django.contrib.auth.models import User


# Create your models here.
class ProductStock(models.Model):
    product_name = models.CharField('Product Name', max_length=250)
    quantity = models.IntegerField()

    def update_stock(self, quantity_change):
        self.quantity += quantity_change
        self.save()

class SaleHistory(AbstractUserModel):
    package = models.CharField('Package', max_length=250)
    quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f"SaleHistory - {self.package}"

class PaymentHistory(models.Model):
    customer = models.ForeignKey(User, on_delete= models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)