from django.contrib import admin
from .models import ProductStock, SaleHistory, PaymentHistory
# Register your models here.

admin.site.register(ProductStock)
class SaleHistoryAdmin(admin.ModelAdmin):
    list_display = ('order','package')
admin.site.register(SaleHistory,SaleHistoryAdmin)

class PaymentHistoryAdmin(admin.ModelAdmin):
    list_display = ('id','customer')
admin.site.register(PaymentHistory, PaymentHistoryAdmin)