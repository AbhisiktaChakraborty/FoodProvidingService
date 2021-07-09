from .models import Order
from datetime import datetime

class OrderManager:

    def findActiveOrders(self):
        pass

    def filterByRatings(self):
        pass

    def sortOrders(self):
        pass

    def filterOrders(self):
        pass
    
    def fetchOrderDetails(self, order_id):
        # fetch already exiting order (for modify order form)
        order=Order.objects.filter(order_id=order_id)
        return order

    def raiseOrder(self,order):
        orderObject = Order()
        if(order['veg_healthy']==""):
            order['veg_healthy']=0
        if(order['veg_ill']==""):
            order['veg_ill']=0
        if(order['nonveg_healthy']==""):
            order['nonveg_healthy']=0
        if(order['nonveg_ill']==""):
            order['nonveg_ill']=0
        if(order['allergies']==""):
            order['allergies']='None'
    
        orderObject.food_seeker_id=order['food_seeker_id']
        orderObject.veg_healthy=order['veg_healthy']
        orderObject.veg_ill=order['veg_ill']
        orderObject.nonveg_healthy=order['nonveg_healthy']
        orderObject.nonveg_ill=order['nonveg_ill']
        orderObject.allergies=order['allergies']
        orderObject.delivery_address=order['delivery_address']
        orderObject.status=0

        orderObject.save()


    def modifyOrder(self,order,order_id):
        # here order is the modified order
        if(order['veg_healthy']==""):
            order['veg_healthy']=0
        if(order['veg_ill']==""):
            order['veg_ill']=0
        if(order['nonveg_healthy']==""):
            order['nonveg_healthy']=0
        if(order['nonveg_ill']==""):
            order['nonveg_ill']=0
        if(order['allergies']==""):
            order['allergies']='None'
    
        orderObject=Order.objects.filter(order_id=order_id)
        orderObject.update(veg_healthy=order['veg_healthy'],veg_ill=order['veg_ill'],nonveg_healthy=order['nonveg_healthy'],nonveg_ill=order['nonveg_ill'],allergies=order['allergies'],delivery_address=order['delivery_address'])


    def cancelOrder(self, order_id):
        orderObject=Order.objects.filter(order_id=order_id)
        orderObject.delete()

    
    def updateOrderStatus(self):
        pass

    def findOrders(self, person_role, person_id):
        # displays order list of food seeker/provider in dashboard
        if(person_role=='food seeker'):
            orders=Order.objects.filter(food_seeker_id=person_id, order_status=0)    #filtering only active orders for my case
            return orders
        else:
            pass

    def confirmOrder(self, fp_id, order_id):
        orderObject=Order.objects.filter(order_id=order_id)
        orderObject.food_provider_id=fp_id
        order_object.confirm_date_time=datetime.now()
        order_object.order_status = 1
        
        


