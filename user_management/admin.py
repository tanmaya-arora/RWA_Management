from django.contrib import admin
from user_management.models import Owner, Tenant, FamilyMember
from django.utils.html import format_html
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display= ('res_hno','fname','lname','check_verified')
    list_filter = ('is_verified',('gender', admin.ChoicesFieldListFilter))
    list_per_page = 5
    show_full_result_count = True
    # change_form_template = 'admin/pagination.html'  

    # def get_list_filter(self, request):
    #     # Set default filter values
    #     list_filter = super().get_list_filter(request)
    #     if 'is_verified' not in list_filter:
    #         list_filter += ['is_verified']
    #     if 'gender' not in list_filter:
    #         list_filter += ['gender']
    #     return list_filter

    def check_verified(self,obj):
         if obj.is_verified:
              return format_html('<div class="d-flex"><img src ="/static/admin/img/icon-yes.svg" style="margin-left:50px"></style></div></img>')
         else:
              return format_html('<div class="d-flex"><img src ="/static/admin/img/icon-no.svg" style="margin-left:50px"></style></div></img>')

    def mark_as_flagged(self, request, queryset):
            queryset.update(is_flagged=True)

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