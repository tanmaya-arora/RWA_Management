from django.contrib import admin

from reporting.models import ProductStock
from .models import Chat, Broadcast, Committee, Country, State, City, Society, Meeting, Payment, Package, Package_Category, Package_attributes, Cart, Event, Order
from django import forms
from django.contrib.auth.models import User, Group
# Register your models here.

class ChatAdminForms(forms.ModelForm):
    member = forms.ModelChoiceField(
        queryset=User.objects.all()
    )
class ChatAdmin(admin.ModelAdmin):
    form = ChatAdminForms
    
admin.site.register(Chat, ChatAdmin)
admin.site.register(Broadcast)

class CommitteeAdminForms(forms.ModelForm):
    position = forms.ModelChoiceField(
        queryset= Group.objects.all()
    )
    committee_role = forms.CharField(widget=forms.TextInput)
class CommitteeAdmin(admin.ModelAdmin):
    form = CommitteeAdminForms
admin.site.register(Committee, CommitteeAdmin)
admin.site.register(Country)
class StateAdminForms(forms.ModelForm):
    country = forms.ModelChoiceField(queryset=Country.objects.all())

class StateAdmin(admin.ModelAdmin):
    form = StateAdminForms
admin.site.register(State, StateAdmin)

class CityAdminForms(forms.ModelForm):
    state = forms.ModelChoiceField(
        queryset= State.objects.all()
    )
class cityAdmin(admin.ModelAdmin):
    form = CityAdminForms
    
admin.site.register(City, cityAdmin)

class SocietyAdminForms(forms.ModelForm):
    city = forms.ModelChoiceField(queryset=City.objects.all())

class SocietyAdmin(admin.ModelAdmin):
    form = SocietyAdminForms
admin.site.register(Society,SocietyAdmin)

class MeetingAdminForms(forms.ModelForm):
    organizer = forms.ModelChoiceField(queryset=Committee.objects.all())
class MeetingAdmin(admin.ModelAdmin):
    form = MeetingAdminForms
admin.site.register(Meeting, MeetingAdmin)

class PaymentAdminForms(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    amount = forms.DecimalField(widget=forms.TextInput)
class PaymentAdmin(admin.ModelAdmin):
    form = PaymentAdminForms
    readonly_fields = ['payment_date',]
    list_display = ('payment_id', 'amount', 'payment_method')
admin.site.register(Payment, PaymentAdmin)

admin.site.register(Package)

class OrderAdminForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    package = forms.ModelChoiceField(queryset=Package_Category.objects.all())
    payment = forms.ModelChoiceField(queryset=Payment.objects.all())
    quantity = forms.IntegerField(widget=forms.TextInput)
    class Meta:
        model = Order
        fields = ['user', 'package', 'payment', 'quantity']
class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm
    list_display = ('user','package','quantity')
    list_filter = [('package')]
    search_fields =('package__name','user__username')
    list_per_page = 5
    readonly_fields = ['date']
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        package_category = obj.package
        quantity_ordered = obj.quantity

        try:
            product_stock = ProductStock.objects.get(product=package_category)
            product_stock.quantity -= quantity_ordered
            product_stock.save()
        except ProductStock.DoesNotExist:
            pass

    
admin.site.register(Order, OrderAdmin)  

class PackageCategoryAdminForms(forms.ModelForm):
    category = forms.ModelChoiceField(queryset= Package.objects.all())
    price = forms.DecimalField(widget= forms.TextInput)
    quantity = forms.IntegerField(widget= forms.TextInput)
class PackageCategoryAdmin(admin.ModelAdmin):
    form = PackageCategoryAdminForms
    list_display=('name', 'price', 'category' )
admin.site.register(Package_Category, PackageCategoryAdmin)


class Package_attributesAdminForms (forms.ModelForm):
    package_details = forms.ModelChoiceField(queryset=Package_Category.objects.all())
    price = forms.DecimalField(widget=forms.TextInput)
    no_of_days = forms.IntegerField(widget=forms.TextInput)
    no_of_users = forms.IntegerField(widget= forms.TextInput)
class Package_attributesAdmin(admin.ModelAdmin):
    form = Package_attributesAdminForms
admin.site.register(Package_attributes, Package_attributesAdmin)

class CartAdminForms(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        )
    quantity = forms.IntegerField(widget = forms.TextInput)
    package_details = forms.CharField(widget = forms.TextInput)
    image_path = forms.CharField(widget = forms.TextInput)
    total_price = forms.DecimalField(widget = forms.TextInput)
class CartAdmin(admin.ModelAdmin):
    form = CartAdminForms
    list_display=('user','package','total_price')
admin.site.register(Cart,CartAdmin)

class EventAdminForms(forms.ModelForm):
    organised_by = forms.ModelChoiceField(queryset= Committee.objects.all())
class EventAdmin(admin.ModelAdmin):
    form = EventAdminForms
    list_display = ('event_name','event_date')
    list_filter = ('event_date','event_name')
    search_fields = [('event_name')]
    list_per_page = 5

admin.site.register(Event,EventAdmin)
