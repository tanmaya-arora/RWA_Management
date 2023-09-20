from django.contrib import admin
from user_management.models import Owner, Tenant
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display= ('res_hno','fname','lname')
admin.site.register(Owner, MemberAdmin)

class TenantAdmin(admin.ModelAdmin):
    list_display= ('res_hno','fname','lname')
admin.site.register(Tenant, TenantAdmin)