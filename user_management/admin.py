from django.contrib import admin
from user_management.models import Owner, Tenant, FamilyMember

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display= ('res_hno','fname','lname','is_verified')
    list_filter = ('gender','is_verified')
    list_per_page = 5
admin.site.register(Owner, MemberAdmin)

class TenantAdmin(admin.ModelAdmin):
    list_display= ('res_hno','fname','lname, is_verified')
    list_filter = ('gender','is_verified')
    list_per_page = 5
admin.site.register(Tenant, TenantAdmin)

class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ('fname','relation','gender','family_head')
    list_filter = ('family_head', 'gender')
    list_per_page = 5
admin.site.register(FamilyMember, FamilyMemberAdmin)