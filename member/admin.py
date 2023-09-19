from django.contrib import admin
from .models import Member, Tenant, Campaign, Chat, Broadcast, Committee, Country, State, City, Society, Meeting, FamilyMember, Payment, Package, Package_Category, Package_attributes, Cart, Event

# Register your models here.

admin.site.register(Member)
admin.site.register(Tenant)
admin.site.register(Campaign)
admin.site.register(Chat)
admin.site.register(Broadcast)
admin.site.register(Committee)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Society)
admin.site.register(Meeting)
admin.site.register(FamilyMember)
admin.site.register(Payment)
admin.site.register(Package)
admin.site.register(Package_Category)
admin.site.register(Package_attributes)
admin.site.register(Cart)
admin.site.register(Event)