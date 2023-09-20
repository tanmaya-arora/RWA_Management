from django.db import models
from django.contrib.auth.models import User
from internal.models import Society, City, State, Country

# Create your models here.

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member')
    member_id = models.AutoField(primary_key=True, editable=False)
    fname = models.CharField(max_length=50, null=False)
    lname = models.CharField(max_length=50, null=False)
    date_of_birth = models.DateField(auto_now_add=False, null=False, blank=False)
    gender = models.CharField(max_length=12, choices=(
        ('', ''), ('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')),
        default=''
    )
    phone_no = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, null=False)
    res_hno = models.SmallIntegerField()
    res_area = models.ForeignKey(Society, on_delete=models.CASCADE)
    res_city = models.ForeignKey(City, on_delete=models.CASCADE)
    res_state = models.ForeignKey(State, on_delete=models.CASCADE)
    res_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    # committee_role = models.ForeignKey(Committee, on_delete=models.CASCADE)
    # marital_status = models.CharField(max_length=50, default='Single')
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.fname} {self.lname}"

class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tenant')
    tenant_id = models.AutoField(primary_key=True, editable=False)
    # member = models.ForeignKey(Member, on_delete=models.CASCADE, null=False)
    fname = models.CharField(max_length=50, null=False)
    lname = models.CharField(max_length=50, null=False)
    
    date_of_birth = models.DateField(auto_now=False)
    gender = models.CharField(max_length=12, choices=(
        ('', ''), ('M', 'male'), ('F', 'female')), default='')
    phone_no = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, null=False)
    res_hno = models.IntegerField()
    res_area = models.ForeignKey(Society, on_delete=models.CASCADE)
    res_city = models.ForeignKey(City, on_delete=models.CASCADE)
    res_state = models.ForeignKey(State, on_delete=models.CASCADE)
    res_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    marital_status = models.CharField(max_length=50, default='Single')
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.fname} {self.lname}"

class FamilyMember(models.Model):
    family_head = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=50, null=False)
    lname = models.CharField(max_length=50, null=False)
    gender = models.CharField(max_length=12, choices=(
        ('', ''), ('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')), default=''
    )
    date_of_birth = models.DateField(auto_now=False)
    relation = models.CharField(max_length=50)
    aniversary_date = models.DateField(auto_now=False)
    marital_status = models.CharField(max_length=50, default='Single')
    #spouse_name = models.CharField(max_length=50, default='')    

    def __str__(self):
        return f"{self.fname} {self.lname}"