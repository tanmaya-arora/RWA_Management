from django.contrib import admin
from .models import Member, Tenant, Donation, Chat, Broadcast, Committee, Country, State, City, Society, Meeting

# Register your models here.

admin.site.register(Member)
admin.site.register(Tenant)
admin.site.register(Donation)
admin.site.register(Chat)
admin.site.register(Broadcast)
admin.site.register(Committee)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Society)
admin.site.register(Meeting)