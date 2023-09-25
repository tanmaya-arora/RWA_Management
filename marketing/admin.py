from django.contrib import admin
from marketing.models import Campaign

# Register your models here.
class CampaignAdmin(admin.ModelAdmin):
    list_display =('event','member','donation_amount')
admin.site.register(Campaign, CampaignAdmin)    