from django.db import models
from django.contrib.auth.models import User, Group
import uuid

# Create your models here.

class Country(models.Model):
    country_id = models.AutoField(primary_key=True, editable=False)
    country = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.country


class State(models.Model):
    state_id = models.AutoField(primary_key=True, editable=False)
    state = models.CharField(max_length=50, null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.state


class City(models.Model):
    city_id = models.AutoField(primary_key=True, editable=False)
    city = models.CharField(max_length=50, null=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.city


class Society(models.Model):
    area_id = models.AutoField(primary_key=True, editable=False)
    area = models.CharField(max_length=100, null=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.area


class Committee(models.Model):
    committee_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=50, null=False)
    position = models.ForeignKey(Group, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=20)
    committee_role = models.TextField()

    def __str__(self):
        return str(self.position)


class Event(models.Model):
    event_id = models.AutoField(primary_key=True, editable=False)
    event_name = models.CharField(max_length=50)
    event_date = models.DateTimeField(auto_now=False)
    location = models.CharField(max_length=100)
    organised_by = models.ForeignKey(Committee, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.event_name

class Payment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    payment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reference_id = models.CharField(max_length=50, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now=True)
    bank_acname = models.CharField(max_length=100, null=True, blank=True)
    bank_acnumber = models.CharField(max_length=20, null=True, blank=True)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return str(self.payment_id)


class Package(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Package_Category(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    category = models.ForeignKey(Package, on_delete=models.CASCADE, null=False)
    package_details = models.TextField()
    image_path = models.TextField()
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.BooleanField(default=0)

    def __str__(self):
        return self.name


class Package_attributes(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    package_details = models.CharField(max_length=50,unique=True,editable=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=40)
    no_of_days = models.IntegerField()
    no_of_users = models.IntegerField()

    def __str__(self):
        return self.name


class package_rel_attriutes(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    package = models.ForeignKey(Package, on_delete=models.CASCADE,null=False)
    Package_category = models.ForeignKey(Package_Category, on_delete=models.CASCADE,null=False)
    Package_attributes = models.ForeignKey(Package_attributes, on_delete=models.CASCADE,null=False)
    status = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Cart(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)    
    package = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=1)
    package_details = models.TextField()
    image_path = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id)

class Order(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False) 
    package = models.ForeignKey(Package_Category, on_delete=models.CASCADE,null=False)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now= True)
    #order_details = models.CharField(max_length=50)

class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True, editable=False)
    member = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    message = models.CharField(max_length=500)

    def __str__(self):
        return str(self.chat_id)


class Broadcast(models.Model):
    broadcast_id = models.AutoField(primary_key=True, editable=False)
    message = models.CharField(max_length=500)

    def __str__(self):
        return str(self.broadcast_id)


class Meeting(models.Model):
    meeting_id = models.AutoField(primary_key=True, editable=False)
    date = models.DateTimeField(auto_now= False)
    location = models.CharField(max_length=50)
    organizer = models.ForeignKey(Committee, on_delete=models.CASCADE, null=False)
    proceeding = models.TextField()

    def __str__(self):
        return str(self.meeting_id)
