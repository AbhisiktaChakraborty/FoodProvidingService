from django.db import models
from django.forms.fields import IntegerField

class Order(models.Model):
	order_id=models.AutoField(primary_key=True)
	veg_healthy=models.IntegerField(null=True)
	veg_ill=models.IntegerField(null=True)
	nonveg_healthy=models.IntegerField(null=True)
	nonveg_ill=models.IntegerField(null=True)
	allergies=models.CharField(max_length=200,null=True)
	delivery_address=models.CharField(max_length=200)
	status=models.CharField(max_length=50)  #active, dispatched or delivered
	food_seeker_id=models.IntegerField()
	food_provider_id=models.IntegerField(null=True)


class FoodSeeker(models.Model):
	fs_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=100)
	mobile=models.CharField(null=True,max_length=10)
	email=models.CharField(max_length=100)

class FoodProvider(models.Model):
    fp_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    mobile=models.CharField(null=True,max_length=10)
    email=models.CharField(max_length=100)
    ratings = models.IntegerField(null=True,default=0)

    def setDetails(self,User):

        fp_new=FoodProvider()
        fp_new.name=User['name']
        fp_new.mobile=User['mobile-number']
        fp_new.email=User['email']

        fp_new.save()

        return fp_new


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



