from django.contrib import admin
from marketing.models import Campaign

# Register your models here.
class CampaignAdmin(admin.ModelAdmin):
    list_display =('event','user','donation_amount')
    list_per_page = 5
    list_filter = ('event','date')
    search_fields = ('event','user','date')

admin.site.register(Campaign, CampaignAdmin)    