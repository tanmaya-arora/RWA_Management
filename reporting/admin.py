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
    list_filter = ('package',)
    search_fields = ('package',)
    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_save'] = True
        extra_context['show_save_as_new'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_and_continue'] = False
        extra_context['show_close'] = False
        extra_context['show_delete_link_and_original'] = False

        return super().change_view(request, object_id, form_url=form_url, extra_context=extra_context)
admin.site.register(SaleHistory,SaleHistoryAdmin)

class PaymentHistoryAdmin(admin.ModelAdmin):
    list_display = ('id','customer')
    search_fields = ['customer']
    # def has_add_permission(self,request):
    #     return False
admin.site.register(PaymentHistory, PaymentHistoryAdmin)