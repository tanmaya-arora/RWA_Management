from django.db import models
from member.models import Event
from user_management.models import Owner

# Create your models here.
class Campaign(models.Model):
    donation_id = models.AutoField(primary_key=True, editable=False)
    member = models.ForeignKey(Owner, on_delete=models.CASCADE, null=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=False)
    notes = models.CharField(max_length=100, default='')
    donation_amount = models.FloatField()

    def __str__(self):
        return str(self.donation_id)
