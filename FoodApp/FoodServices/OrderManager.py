from .models import Order

class OrderManager:

    def findActiveOrders(self):
        pass

    def filterByRatings(self):
        pass

    def sortOrders(self):
        pass

    def filterOrders(self):
        pass

    def raiseOrder(self):
        pass

    def modifyOrder(self):
        pass

    def fetchOrderDetails(self,id,type):
        orders=Order.objects.all()
        orderListFP=[]
        #orderListFS=[]
        if type=="FoodProvider":
            for o in orders:
                if o.food_seeker_id==id:
                    orderListFP.append(o)
        print(orders)
        return orderListFP
    def updateOrderStatus(self):
        pass

    def findOrder(self):
        pass

    def confirmOrder(self):
        pass

