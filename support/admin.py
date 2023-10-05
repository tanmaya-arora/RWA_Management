from django.contrib import admin
from support.models import Ticket
from django.utils.html import format_html

    # Register your models here.
class TicketAdmin(admin.ModelAdmin):
    list_display= ('ticket_colored', 'priority_colored','name_colored','check_resolved','formatted_date')
    list_filter = ('resolved','priority')
    search_fields = ('person_name','ticket_id')
    list_per_page = 5
    actions = ['mark_as_flagged']
    readonly_fields = ('person_name','person_email','phone_no','priority','message','date')    
    # ordering = ("person_name", "person_email", "contact_no")  
    # date_hierarchy =('date')
    fieldsets = (
        ('Requested Fields:', {
            'fields': (
                ("person_name","person_email","phone_no"),
                ("priority","date","message"),

            ),
        }),
        ('Additional Fields:', {
            'fields': (
                ("reply_message", "resolved", "replied_by"),
            ),
        }),
    )
    change_form_template = 'admin/support/change_form.html'   

    def field_format(self,obj,fields):
         return obj.fields('<div class="d-flex"></div>')
         

    def formatted_date(self, obj):
        return obj.date.strftime("%d-%m-%Y  %H:%M")  

    formatted_date.short_description = 'Formatted Date'
    
    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_save'] = True
        extra_context['show_save_as_new'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_and_continue'] = False
        
        return super().change_view(request, object_id, form_url=form_url, extra_context=extra_context)

    def has_delete_permission(self, request, obj=None):
         return False
    
    def priority_colored(self, obj):
            if obj.resolved:
                return format_html('<span style="color: grey;">{}</span>', obj.priority)
            else:
                return format_html('<span style="color: black;">{}</span>', obj.priority)
    priority_colored.short_description = 'Priority'

    def ticket_colored(self, obj):
            if obj.resolved:
                return format_html('<span style="color: grey;">{}</span>', obj.ticket_id)
            else:
                return format_html('<span style="color: black;">{}</span>', obj.ticket_id)
    ticket_colored.short_description = 'ticket_id'

    def name_colored(self, obj):
            if obj.resolved:
                return format_html('<span style="color: grey;">{}</span>', obj.person_name)
            else:
                return format_html('<span style="color: black;">{}</span>', obj.person_name)
    name_colored.short_description = 'name'

    def check_resolved(self,obj):
         if obj.resolved:
              return format_html('<div class="d-flex"><img src ="/static/admin/img/icon-yes.svg" class="mx-auto"></div></img>')
         else:
              return format_html('<div class="d-flex"><img src ="/static/admin/img/icon-no.svg" class="mx-auto"></div></img>')

    def mark_as_flagged(self, request, queryset):
            queryset.update(is_flagged=True)
    
    class Media:
         js = ['custom_admin.js']


admin.site.register(Ticket, TicketAdmin)

