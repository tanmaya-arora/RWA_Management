from django.db import models
from django.contrib.auth.models import User, Group
import uuid
from django.utils.html import format_html


# Create your models here.

class Ticket(models.Model):
    ticket_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person_name = models.CharField(max_length=50)
    person_email = models.EmailField(max_length=100)
    phone_no = models.BigIntegerField()
    date = models.DateTimeField(auto_now=True)
    message = models.TextField()
    resolved = models.BooleanField(default=False)
    priority = models.CharField(max_length=12, choices=(
        ('low', 'Low'), ('normal', 'Normal'), ('high', 'High')),
        default='Normal'
    )
    reply_message = models.TextField(null=True)
    datetime_reply = models.DateTimeField(auto_now=True)
    replied_by = models.ForeignKey(Group, on_delete=models.CASCADE, null =True, default = None)

    def __str__(self):
        return str(self.ticket_id)
