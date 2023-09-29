from django.contrib import admin
from user_management.models import Owner, Tenant, FamilyMember

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display= ('res_hno','fname','lname','is_verified')
    list_filter = ('gender','is_verified')
    list_per_page = 5
    show_full_result_count = True



    # def get_paginator(self, request, queryset, per_page, orphans=0, allow_empty_first_page=True):
    #     # Remove the previous button by setting orphans to a high value
    #     orphans = 999999
    #     return super().get_paginator(request, queryset, per_page, orphans, allow_empty_first_page)

    # change_form_template = 'admin/pagination.html'   

admin.site.register(Owner, MemberAdmin)

class TenantAdmin(admin.ModelAdmin):
    list_display= ('res_hno','fname','lname', 'is_verified')
    list_filter = ('gender','is_verified')
    list_per_page = 5
admin.site.register(Tenant, TenantAdmin)

class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ('fname','relation','gender','family_head')
    list_filter = ('relation', 'gender')
    list_per_page = 5
admin.site.register(FamilyMember, FamilyMemberAdmin)