from django.db import models

class Order(models.Model):
    pass

class FoodProvider(models.Model):
    pass

class FoodSeeker(models.Model):
    pass

class Address(models.Model):  
    add_id =  models.BigAutoField(primary_key=True)
    building = models.CharField(max_length=100)
    street = models.CharField(max_length=100, default = '')
    landmark = models.CharField(max_length=100, default = '')
    city = models.CharField(max_length=100, default = '')
    state = models.CharField(max_length=100, default = '')
    country = models.CharField(max_length=100, default = '')
    pincode = models.CharField(max_length=9, default = '')

class Messages(models.Model):
    pass



