from django.db import models
from internal.models import Payment,Order,Package_Category


# Create your models here.
class ProductStock(models.Model):
    product = models.OneToOneField(Package_Category, on_delete=models.CASCADE, primary_key=True)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - Stock: {self.quantity}"

class SaleHistory(Order):
    # package = models.CharField('Package', max_length=250)
    # quantity = models.PositiveIntegerField(null=True)

    class Meta: 
        proxy = True
        verbose_name = 'Product Sale History'
        verbose_name_plural = 'Product Sales History'

class PaymentHistory(Payment):
    # customer = models.ForeignKey(User, on_delete= models.CASCADE)
    # payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    
    class Meta:
        proxy = True
        verbose_name = 'Financial Summary'
        verbose_name_plural = 'Financial Summaries'