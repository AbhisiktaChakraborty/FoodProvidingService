from django.db import models

# Create your models here.

class FoodSeeker(models.Model):
    fs_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100, default='')
    phone_no=models.CharField(max_length=100, default='')
    email=models.CharField(max_length=100, default= '')

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    veg_healthy=models.IntegerField(null=True)
    veg_ill=models.IntegerField(null=True)
    nonveg_healthy=models.IntegerField(null=True)
    nonveg_ill=models.IntegerField(null=True)
    allergies=models.CharField(max_length=200,null=True)
    delivery_address=models.CharField(max_length=200, default='')
    order_status=models.IntegerField(default=0) #active:0, confirmed:1, dispatched:2 or delivered:3
    food_seeker_id=models.IntegerField(default=0)
    food_provider_id=models.IntegerField(null=True)
#   confirm_date_time 
#   dispatch_date_time
#   deliver_date_time


class Address(models.Model):  
    add_id =  models.BigAutoField(primary_key=True)
    person_id=models.IntegerField(default=0)
    person_role=models.CharField(max_length=50, default='')     #food seeker or food provider
    building = models.CharField(max_length=100, default= '')
    street = models.CharField(max_length=100, default = '')
    landmark = models.CharField(max_length=100, default = '')
    city = models.CharField(max_length=100, default = '')
    state = models.CharField(max_length=100, default = '')
    country = models.CharField(max_length=100, default = '')
    pincode = models.CharField(max_length=9, default = '')


class Messages(models.Model):
    pass


class FoodProvider(models.Model):
    pass


