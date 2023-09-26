from django.contrib import admin
from support.models import Ticket

# Register your models here.
class TicketAdmin(admin.ModelAdmin):
    list_display= ('ticket_id', 'priority','person_name','resolved')
    list_filter = ('resolved','priority')
    search_fields = ('person_name','ticket_id')
    
admin.site.register(Ticket, TicketAdmin)

