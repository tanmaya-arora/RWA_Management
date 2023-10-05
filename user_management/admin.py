from django.contrib import admin
from user_management.models import Owner, Tenant, FamilyMember
from django.utils.html import format_html

class MemberAdmin(admin.ModelAdmin):

    list_display= ('res_hno','fname','lname','check_verified')
    list_filter = ('is_verified','gender')
    list_per_page = 5
    show_full_result_count = True
    search_fields =('res_hno','fname','lname')
    class Media:
         js = ['/static/files/js/owner_admin.js']

    def check_verified(self,obj):
         if obj.is_verified:
              return format_html('<div class="d-flex"><img src ="/static/admin/img/icon-yes.svg" style="margin-left:50px"></style></div></img>')
         else:
              return format_html('<div class="d-flex"><img src ="/static/admin/img/icon-no.svg" style="margin-left:50px"></style></div></img>')

    def mark_as_flagged(self, request, queryset):
            queryset.update(is_flagged=True)

admin.site.register(Owner, MemberAdmin)

class TenantAdmin(admin.ModelAdmin):
    list_display= ('res_hno','fname','lname','check_verified')
    list_filter = ('is_verified','gender')
    list_per_page = 5
    show_full_result_count = True
    search_fields =('res_hno','fname','lname')
    class Media:
         js = ['/static/files/js/owner_admin.js']

    def check_verified(self,obj):
         if obj.is_verified:
              return format_html('<div class="d-flex"><img src ="/static/admin/img/icon-yes.svg" style="margin-left:50px"></style></div></img>')
         else:
              return format_html('<div class="d-flex"><img src ="/static/admin/img/icon-no.svg" style="margin-left:50px"></style></div></img>')

    def mark_as_flagged(self, request, queryset):
            queryset.update(is_flagged=True)
admin.site.register(Tenant, TenantAdmin)

class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ('fname','relation','gender','family_head')
    list_filter = ('relation', 'gender')
    list_per_page = 5
    search_fields = ('family_head__username','fname','gender')

    class Media:
        js = ['/static/files/js/family_admin.js']
admin.site.register(FamilyMember, FamilyMemberAdmin)