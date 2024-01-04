from django.contrib import admin
from user_management.models import Owner, Tenant, Family
from django.utils.html import format_html
from django import forms
from django.contrib.auth.models import User
from internal.models import Society, City,State, Country


class OwnerAdminForms(forms.ModelForm):
     user = forms.ModelChoiceField(queryset= User.objects.all())
     res_hno = forms.IntegerField(widget= forms.TextInput)
     res_area = forms.ModelChoiceField(queryset=Society.objects.all())
     res_city = forms.ModelChoiceField(queryset=City.objects.all())
     res_state = forms.ModelChoiceField(queryset=State.objects.all())
     res_country = forms.ModelChoiceField(queryset=Country.objects.all())

class OwnerAdmin(admin.ModelAdmin):
     form = OwnerAdminForms
     list_display= ('res_hno','fname','lname','check_verified')
     list_filter = ('isVerified','gender')
     list_per_page = 5
     show_full_result_count = True
     search_fields =('res_hno','fname','lname')
     class Media:
          js = ['/static/files/js/owner_admin.js']

     def check_verified(self,obj):
          if obj.isVerified:
               return format_html('<div class="d-flex"><img src ="/static/admin/img/icon-yes.svg" style="margin-left:50px"></style></div></img>')
          else:
               return format_html('<div class="d-flex"><img src ="/static/admin/img/icon-no.svg" style="margin-left:50px"></style></div></img>')

     def mark_as_flagged(self, request, queryset):
               queryset.update(is_flagged=True)

admin.site.register(Owner, OwnerAdmin)

class TenantAdminForms(forms.ModelForm):
     user = forms.ModelChoiceField(queryset= User.objects.all())
     res_hno = forms.IntegerField(widget= forms.TextInput)
     res_area = forms.ModelChoiceField(queryset=Society.objects.all())
     res_city = forms.ModelChoiceField(queryset=City.objects.all())
     res_state = forms.ModelChoiceField(queryset=State.objects.all())
     res_country = forms.ModelChoiceField(queryset=Country.objects.all())
class TenantAdmin(admin.ModelAdmin):
     
     form = TenantAdminForms
     list_display= ('res_hno','fname','lname','check_verified')
     list_filter = ('isVerified','gender')
     list_per_page = 5
     show_full_result_count = True
     search_fields =('res_hno','fname','lname')
     class Media:
          js = ['/static/files/js/owner_admin.js']

     def check_verified(self,obj):
          if obj.isVerified:
               return format_html('<div class="d-flex"><img src ="/static/admin/img/icon-yes.svg" style="margin-left:50px"></style></div></img>')
          else:
               return format_html('<div class="d-flex"><img src ="/static/admin/img/icon-no.svg" style="margin-left:50px"></style></div></img>')

     def mark_as_flagged(self, request, queryset):
               queryset.update(is_flagged=True)
admin.site.register(Tenant, TenantAdmin)

class FamilyMemberAdminForms(forms.ModelForm):
     family_head = forms.ModelChoiceField(queryset=User.objects.all())
class FamilyMemberAdmin(admin.ModelAdmin):
     form = FamilyMemberAdminForms
     list_display = ('fname','relation','gender','family_head')
     list_filter = ('relation', 'gender')
     list_per_page = 5
     search_fields = ('family_head__username','fname','gender')

     class Media:
          js = ['/static/files/js/family_admin.js']
admin.site.register(Family, FamilyMemberAdmin)