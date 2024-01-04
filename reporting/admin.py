from django.contrib import admin
from .models import ProductStock, SaleHistory, PaymentHistory, Package_Category
from django import forms
from django.contrib.auth.models import User
# Register your models here.

class ProductStockAdminForms(forms.ModelForm):
    quantity = forms.IntegerField(widget=forms.TextInput)
    product = forms.ModelChoiceField(queryset=Package_Category.objects.all())
class ProductStockAdmin(admin.ModelAdmin):
    form = ProductStockAdminForms
    list_display = ('product', 'quantity')
    list_per_page = 5
    
admin.site.register(ProductStock, ProductStockAdmin)

class SaleHistoryAdminForm(forms.ModelForm):
    quantity = forms.IntegerField(widget=forms.TextInput)
    user = forms.ModelChoiceField(queryset= User.objects.all())
class SaleHistoryAdmin(admin.ModelAdmin):
    form = SaleHistoryAdminForm
    list_display = ('user','package','payment', 'date','quantity')
    list_per_page = 5
    list_filter = ('package',)
    search_fields = ('package__name','user__username')
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request,obj = None):
        return False
admin.site.register(SaleHistory,SaleHistoryAdmin)

class PaymentHistoryAdminForms(forms.ModelForm):
    user = forms.ModelChoiceField(queryset = User.objects.all())
class PaymentHistoryAdmin(admin.ModelAdmin):
    form = PaymentHistoryAdminForms
    list_display = ('user','amount','payment_method','bank_acname','bank_acnumber','payment_status','payment_date')
    search_fields = ['amount', 'payment_method', 'bank_acname', 'bank_acnumber', 'user__username']
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request,obj = None):
        return False
admin.site.register(PaymentHistory, PaymentHistoryAdmin)