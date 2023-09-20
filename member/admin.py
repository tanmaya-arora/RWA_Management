from django.contrib import admin
from .models import Chat, Broadcast, Committee, Country, State, City, Society, Meeting, FamilyMember, Payment, Package, Package_Category, Package_attributes, Cart, Event

# Register your models here.

admin.site.register(Chat)
admin.site.register(Broadcast)
admin.site.register(Committee)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Society)
admin.site.register(Meeting)

class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ('fname','relation','gender','family_head')
admin.site.register(FamilyMember, FamilyMemberAdmin)

admin.site.register(Payment)
admin.site.register(Package)

class PackageCategoryAdmin(admin.ModelAdmin):
    list_display=('name', 'price' )
admin.site.register(Package_Category, PackageCategoryAdmin)

admin.site.register(Package_attributes)
admin.site.register(Cart)
admin.site.register(Event)
