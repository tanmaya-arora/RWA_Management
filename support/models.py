from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class TicketPriority(models.Model):
    priority_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    priority_name = models.CharField(max_length=12, choices=(
        ('Low', 'Low'), ('Normal', 'Normal'), ('High', 'High')),
        default='Normal'
    )
    def __str__(self):
        return self.priority_name

class Ticket(models.Model):
    ticket_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person_name = models.CharField(max_length=50)
    person_email = models.EmailField(max_length=100)
    contact_no = models.CharField(max_length=20)
    message = models.TextField()
    priority = models.ForeignKey(TicketPriority, on_delete=models.CASCADE)
    resolved = models.BooleanField(default=False)

class TicketReply(models.Model):
    reply_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    reply_message = models.TextField()
    datetime_reply = models.DateTimeField(auto_now=True)
    replied_by = models.ForeignKey(User, on_delete=models.CASCADE)
