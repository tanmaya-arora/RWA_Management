from django.contrib import admin
from support.models import Ticket

# Register your models here.
class TicketAdmin(admin.ModelAdmin):
    list_display= ('ticket_id', 'priority','person_name','resolved')
    list_filter = ('resolved','priority')
admin.site.register(Ticket, TicketAdmin)

