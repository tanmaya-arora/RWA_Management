from django.db import models
from internal.models import Event
from user_management.models import Owner
from django.contrib.auth.models import User

# Create your models here.
class Campaign(models.Model):
    donation_id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=False)
    notes = models.CharField(max_length=100, default='')
    donation_amount = models.FloatField()
    date = models.DateField(null=False)
    time = models.TimeField(null= False)

    def __str__(self):
        return str(self.donation_id)
