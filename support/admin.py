from django.contrib import admin
from support.models import Ticket,TicketReply

# Register your models here.
class TicketAdmin(admin.ModelAdmin):
    list_display= ('ticket_id', 'priority','person_name','resolved')
admin.site.register(Ticket, TicketAdmin)

admin.site.register(TicketReply)
