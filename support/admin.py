from django.contrib import admin
from support.models import Ticket,TicketPriority,TicketReply

# Register your models here.

admin.site.register(Ticket)
admin.site.register(TicketPriority)
admin.site.register(TicketReply)
