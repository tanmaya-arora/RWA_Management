from django.contrib import admin
from .models import Chat, Broadcast, Committee, Country, State, City, Society, Meeting, Payment, Package, Package_Category, Package_attributes, Cart, Event, Order

# Register your models here.

admin.site.register(Chat)
admin.site.register(Broadcast)
admin.site.register(Committee)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Society)
admin.site.register(Meeting)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'amount', 'payment_method')
admin.site.register(Payment, PaymentAdmin)

admin.site.register(Package)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','package','quantity')
    list_filter = [('package')]
    search_fields =('package','user')
    list_per_page = 5
admin.site.register(Order, OrderAdmin)

class PackageCategoryAdmin(admin.ModelAdmin):
    list_display=('name', 'price', 'category' )
admin.site.register(Package_Category, PackageCategoryAdmin)

admin.site.register(Package_attributes)
class CartAdmin(admin.ModelAdmin):
    list_display=('user','package','total_price')
admin.site.register(Cart,CartAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name','event_date')
    list_filter = ('event_name','event_date')
    search_fields = [('event_name')]
    list_per_page = 5

admin.site.register(Event,EventAdmin)
