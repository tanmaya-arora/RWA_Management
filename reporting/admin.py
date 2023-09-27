from django.contrib import admin
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from .models import ProductStock, SaleHistory, PaymentHistory
# Register your models here.

class ProductStockAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'quantity')
    list_filter = [('product_name')]
    search_fields = [('product_name')]
    list_per_page = 5
    
admin.site.register(ProductStock, ProductStockAdmin)
class SaleHistoryAdmin(admin.ModelAdmin):
    list_display = ('user','package')
    list_per_page = 5
    list_filter = [('package')]
    search_fields = [('package')]
admin.site.register(SaleHistory,SaleHistoryAdmin)

class PaymentHistoryAdmin(admin.ModelAdmin):
    list_display = ('id','customer')
    search_fields = ['customer']
    # def has_add_permission(self,request):
    #     return False
admin.site.register(PaymentHistory, PaymentHistoryAdmin)