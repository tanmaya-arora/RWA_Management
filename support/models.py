from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Ticket(models.Model):
    ticket_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person_name = models.CharField(max_length=50)
    person_email = models.EmailField(max_length=100)
    contact_no = models.BigIntegerField()
    message = models.TextField()
    resolved = models.BooleanField(default=False)
    priority = models.CharField(max_length=12, choices=(
        ('low', 'Low'), ('normal', 'Normal'), ('high', 'High')),
        default='Normal'
    )

    def __str__(self):
        return self.priority

class TicketReply(models.Model):
    reply_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    reply_message = models.TextField()
    datetime_reply = models.DateTimeField(auto_now=True)
    replied_by = models.ForeignKey(User, on_delete=models.CASCADE, null =False)
