
from django.test import TestCase
from FoodServices.models import *

# Create your tests here.
class TestModels(TestCase):

    def test_model_address(self):
        user_add = Address(building = 'SPHS', street = '82/7A Ballygunge Place', landmark = 'Mercury Point', city = 'Kolkata', 
        state = 'West Bengal', country = 'India', pincode = '700091' )
        user_add.save()

        self.assertEquals(user_add.add_id, 1)
        self.assertEquals(user_add.building, 'SPHS')
        self.assertEquals(user_add.street, '82/7A Ballygunge Place')
        self.assertEquals(user_add.landmark, 'Mercury Point')
        self.assertEquals(user_add.city, 'Kolkata')
        self.assertEquals(user_add.state, 'West Bengal')
        self.assertEquals(user_add.country, 'India')
        self.assertEquals(user_add.pincode, '700091')

    def test_model_FoodProvider(self):
        user_fp = FoodProvider(name='Food Provider', mobile='1234567890', email='fp@gmail.com', ratings = 4.5)
        user_fp.save()

        self.assertEquals(user_fp.fp_id,1)
        self.assertEquals(user_fp.name,'Food Provider')
        self.assertEquals(user_fp.mobile,'1234567890')
        self.assertEquals(user_fp.email,'fp@gmail.com')
        self.assertEquals(user_fp.ratings,4.5)

    def test_model_FoodSeeker(self):
        user_fs = FoodSeeker(name='Food Seeker', mobile='1234554321', email='fs@gmail.com')
        user_fs.save()

        self.assertEquals(user_fs.fs_id,1)
        self.assertEquals(user_fs.name,'Food Seeker')
        self.assertEquals(user_fs.mobile,'1234554321')
        self.assertEquals(user_fs.email,'fs@gmail.com')

    def test_model_order(self):
        user_order=Order(veg_healthy=2,nonveg_ill=3,allergies = 'prawn',delivery_address='123 K.L Road, Srirampore-722309',
        status='active',food_seeker_id=1)
        user_order.save()
		
        self.assertEquals(user_order.order_id,1)
        self.assertEquals(user_order.veg_healthy,2)
        self.assertEquals(user_order.veg_ill,None)
        self.assertEquals(user_order.nonveg_healthy,None)
        self.assertEquals(user_order.nonveg_ill,3)
        self.assertEquals(user_order.allergies,'prawn')
        self.assertEquals(user_order.delivery_address,'123 K.L Road, Srirampore-722309')
        self.assertEquals(user_order.status,'active')
        self.assertEquals(user_order.food_seeker_id,1)
        self.assertEquals(user_order.food_provider_id,None)