from django.test import TestCase 
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from raisemodifyorder.views import *
from raisemodifyorder.models import *
from raisemodifyorder.OrderManager import *

# Create your tests here.

class TestingViews(TestCase):
	def setUp(self):
		self.orderManager=OrderManager()

	def test_raiseOrder(self):

		order={}
		order['veg_healthy']=1
		order['veg_ill']=""
		order['nonveg_healthy']=""
		order['nonveg_ill']=4
		order['allergies']=""
		order['delivery_address']='123 H.K Road, Kolkta-700090, West bengal,India'
		order['food_seeker_id']=1

		self.orderManager.raiseOrder(order)

		order_obtained_from_db=Order.objects.get(order_id=1)

		#check required fields are entered
		self.assertEquals(order_obtained_from_db.order_id,1)
		self.assertTrue(order_obtained_from_db.food_seeker_id)
		self.assertTrue(order_obtained_from_db.delivery_address)
		total_food_packets=order_obtained_from_db.veg_healthy + order_obtained_from_db.veg_ill + order_obtained_from_db.nonveg_healthy + order_obtained_from_db.nonveg_ill
		self.assertTrue(total_food_packets)
		
		if(order_obtained_from_db.order_status!=0):		#if order confirmed, only then food provider should be there.
			self.assertTrue(order_obtained_from_db.food_provider_id)
		else:
			self.assertFalse(order_obtained_from_db.food_provider_id)

		#check correct data entered
		self.assertEquals(order_obtained_from_db.veg_healthy,1)
		self.assertEquals(order_obtained_from_db.veg_ill,0)
		self.assertEquals(order_obtained_from_db.nonveg_healthy,0)
		self.assertEquals(order_obtained_from_db.nonveg_ill,4)
		self.assertEquals(order_obtained_from_db.allergies,'None')
		self.assertEquals(order_obtained_from_db.delivery_address,'123 H.K Road, Kolkta-700090, West bengal,India')
		self.assertEquals(order_obtained_from_db.order_status,0)
		self.assertEquals(order_obtained_from_db.food_seeker_id,1)


	def test_modifyOrder(self):
		order=Order(veg_healthy=1,veg_ill=0,nonveg_healthy=0,nonveg_ill=4,delivery_address='123 H.K Road, Kolkta-700090, West bengal,India',food_seeker_id=1)
		order.save()

		order_to_modify={}
		order_to_modify['veg_healthy']=2
		order_to_modify['veg_ill']=1
		order_to_modify['nonveg_healthy']=0
		order_to_modify['nonveg_ill']=4
		order_to_modify['allergies']='None'
		order_to_modify['delivery_address']='123 H.K Road, Kolkta-700090, West bengal,India'

		self.orderManager.modifyOrder(order_to_modify,1)

		order_obtained_from_db=Order.objects.get(order_id=1)
		
		#checking updated fields modified
		self.assertEquals(order_obtained_from_db.veg_healthy,2)
		self.assertEquals(order_obtained_from_db.veg_ill,1)
		self.assertEquals(order_obtained_from_db.nonveg_healthy,0)
		self.assertEquals(order_obtained_from_db.nonveg_ill,4)
		self.assertEquals(order_obtained_from_db.allergies,'None')
		self.assertEquals(order_obtained_from_db.delivery_address,'123 H.K Road, Kolkta-700090, West bengal,India')


		#checking previous fields remain same
		self.assertEquals(order_obtained_from_db.order_id,1)
		self.assertEquals(order_obtained_from_db.order_status,0)
		self.assertEquals(order_obtained_from_db.food_seeker_id,1)


	def test_cancelOrder(self):
		order=Order(veg_healthy=1,veg_ill=0,nonveg_healthy=0,nonveg_ill=4,delivery_address='123 H.K Road, Kolkta-700090, West bengal,India',food_seeker_id=1)
		order.save()

		self.orderManager.cancelOrder(1)

		order_obtained_from_db=Order.objects.filter(order_id=1)
		self.assertFalse(order_obtained_from_db)


	def test_findOrders(self):
		order1=Order(veg_healthy=1,veg_ill=0,nonveg_healthy=0,nonveg_ill=4,delivery_address='123 H.K Road, Kolkta-700090, West bengal,India',food_seeker_id=1)
		order1.save()

		order2=Order(veg_healthy=5,veg_ill=0,nonveg_healthy=0,nonveg_ill=1,delivery_address='789 H.K Road, Kolkta-700090, West bengal,India',food_seeker_id=1)
		order2.save()

		order3=Order(veg_healthy=1,veg_ill=0,nonveg_healthy=4,nonveg_ill=0,delivery_address='123 H.K Road, Kolkta-700090, West bengal,India',food_seeker_id=1)
		order3.save()

		orders_of_food_seeker_1=self.orderManager.findOrders('food seeker',1)
		number_of_active_orders_of_food_seeker_1= orders_of_food_seeker_1.count()

		self.assertEquals(number_of_active_orders_of_food_seeker_1,3)



class TestingModels(TestCase):

	def test_model_food_seeker(self):

		fs_test=FoodSeeker(name='TestUser', phone_no='1234554321', email='testuser@gmail.com')
		fs_test.save()

		fs_obtained_from_db=FoodSeeker.objects.filter(name='TestUser')
		
		self.assertEquals(fs_obtained_from_db[0].fs_id,1)
		self.assertEquals(fs_obtained_from_db[0].name,'TestUser')
		self.assertEquals(fs_obtained_from_db[0].phone_no,'1234554321')
		self.assertEquals(fs_obtained_from_db[0].email,'testuser@gmail.com')


	def test_model_address(self):
		user_test=Address(person_id=1, person_role='food seeker', building='123',street='K.L Road',landmark='B.P School',city='Howrah',state='West bengal',country='India',pincode='700012')
		user_test.save()

		user_obtained_from_db=Address.objects.filter(person_role='food seeker')
		
		self.assertEquals(user_obtained_from_db[0].add_id,1)
		self.assertEquals(user_obtained_from_db[0].person_id,1)
		self.assertEquals(user_obtained_from_db[0].person_role,'food seeker')
		self.assertEquals(user_obtained_from_db[0].building,'123')
		self.assertEquals(user_obtained_from_db[0].street,'K.L Road')
		self.assertEquals(user_obtained_from_db[0].landmark,'B.P School')
		self.assertEquals(user_obtained_from_db[0].city,'Howrah')
		self.assertEquals(user_obtained_from_db[0].state,'West bengal')
		self.assertEquals(user_obtained_from_db[0].country,'India')
		self.assertEquals(user_obtained_from_db[0].pincode,'700012')


	def test_model_order(self):

		order=Order(veg_healthy=2,nonveg_ill=3,delivery_address='123 K.L Road, Srirampore-722309, West Bengal, India',order_status=0,food_seeker_id=1)
		order.save()

		order_obtained_from_db=Order.objects.filter(order_id=1)
		
		self.assertEquals(order_obtained_from_db[0].order_id,1)
		self.assertEquals(order_obtained_from_db[0].veg_healthy,2)
		self.assertEquals(order_obtained_from_db[0].veg_ill,None)
		self.assertEquals(order_obtained_from_db[0].nonveg_healthy,None)
		self.assertEquals(order_obtained_from_db[0].nonveg_ill,3)
		self.assertEquals(order_obtained_from_db[0].delivery_address,'123 K.L Road, Srirampore-722309, West Bengal, India')
		self.assertEquals(order_obtained_from_db[0].order_status,0)
		self.assertEquals(order_obtained_from_db[0].food_seeker_id,1)
		self.assertEquals(order_obtained_from_db[0].food_provider_id,None)



class TestingUrls(TestCase):

	def test_accesses_correct_pages(self):
		
		self.signin_url=reverse('signin')
		self.raiseorder_url=reverse('raiseorder')
		self.dashboard_url=reverse('dashboard_foodseeker')
		self.modifyorder_url =reverse('modifyorder')
		self.header_url=reverse('header')
		
		self.assertEquals(resolve(self.raiseorder_url).func, displayNewOrderForm)
		self.assertEquals(resolve(self.modifyorder_url).func, displayEditableOrderForm)
		self.assertEquals(resolve(self.dashboard_url).func, displayFSOrderList)
		self.assertEquals(resolve(self.signin_url).func, displaySignInForm)
		self.assertEquals(resolve(self.header_url).func, header)


