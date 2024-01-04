from django.contrib import admin
from marketing.models import Campaign,Event
from django import forms
from django.contrib.auth.models import User

# Register your models here.

class CampaignAdminForms(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    event = forms.ModelChoiceField(queryset= Event.objects.all())
    donation_amount = forms.FloatField(widget= forms.TextInput)
class CampaignAdmin(admin.ModelAdmin):
    form = CampaignAdminForms
    list_display =('event','user','donation_amount')
    list_per_page = 5
    list_filter = ('event','date')
    search_fields = ('event','user','date')

admin.site.register(Campaign, CampaignAdmin)    