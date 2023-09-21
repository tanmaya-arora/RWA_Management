from django.contrib import admin
from .models import Chat, Broadcast, Committee, Country, State, City, Society, Meeting, Payment, Package, Package_Category, Package_attributes, Cart, Event

# Register your models here.

admin.site.register(Chat)
admin.site.register(Broadcast)
admin.site.register(Committee)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Society)
admin.site.register(Meeting)

admin.site.register(Payment)
admin.site.register(Package)

class PackageCategoryAdmin(admin.ModelAdmin):
    list_display=('name', 'price' )
admin.site.register(Package_Category, PackageCategoryAdmin)

admin.site.register(Package_attributes)
class CartAdmin(admin.ModelAdmin):
    list_display=('user','package','total_price')
admin.site.register(Cart,CartAdmin)
admin.site.register(Event)
