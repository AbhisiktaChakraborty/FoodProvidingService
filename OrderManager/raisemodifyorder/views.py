
from django.shortcuts import render,redirect
from .models import *
from .LoginManager import LoginManager
from .OrderManager import OrderManager
from .AddressManager import AddressManager

#RaiseOrderUI
def displayNewOrderForm(request):
	loginManager= LoginManager()
	addressManager=AddressManager()
	fs= loginManager.verifyUser(request.session['mobile'])
	addr=addressManager.findAddressesCorrespondingToPerson(person_id=request.session['fs_id'],person_role='food seeker')
	return render(request,'raisemodifyorder/raiseorder.html',{'FoodSeekers': fs, 'Addresses':addr})

def submitOrderForm(request):
	order ={}
	order['food_seeker_id']=request.session['fs_id']
	order['veg_healthy']=request.POST.get("veg_healthy",False)
	order['veg_ill'] = request.POST.get("veg_ill",False)
	order['nonveg_healthy']=request.POST.get("nonveg_healthy",False)
	order['nonveg_ill']=request.POST.get("nonveg_ill",False)
	order['allergies']=request.POST.get("allergy",False)
	order['delivery_address']=request.POST.get("delivery_address",False)

	orderManager=OrderManager()
	orderManager.raiseOrder(order)

	loginManager= LoginManager()
	fs= loginManager.verifyUser(request.session['mobile'])
    
	return render(request, 'raisemodifyorder/dashboard_foodseeker.html',{'FoodSeekers': fs})



#ModifyOrderUI

def displayEditableOrderForm(request):
	fs_id=request.session['fs_id']
	modify_order_id=request.POST.get("modify_order_id", False)
	
	loginManager= LoginManager()
	addressManager=AddressManager()
	orderManager=OrderManager()

	fs= loginManager.verifyUser(request.session['mobile'])
	addr=addressManager.findAddressesCorrespondingToPerson(person_id=fs_id,person_role='food seeker')
	order=orderManager.fetchOrderDetails(modify_order_id)
	
	return render(request, 'raisemodifyorder/modifyorder.html',{'FoodSeekers': fs, 'Order': order, 'Addresses': addr})


def submitModifyOrderForm(request, order_id, modify_or_cancel):
	orderManager=OrderManager()
	if(modify_or_cancel=="modify"):
		order ={}
		order['veg_healthy']=request.POST.get("veg_healthy",False)
		order['veg_ill'] = request.POST.get("veg_ill",False)
		order['nonveg_healthy']=request.POST.get("nonveg_healthy",False)
		order['nonveg_ill']=request.POST.get("nonveg_ill",False)
		order['allergies']=request.POST.get("allergy",False)
		order['delivery_address']=request.POST.get("delivery_address",False)

		orderManager.modifyOrder(order, order_id)

	else:
		orderManager.cancelOrder(order_id)

	loginManager= LoginManager()
	fs= loginManager.verifyUser(request.session['mobile'])
    
	return render(request, 'raisemodifyorder/dashboard_foodseeker.html',{'FoodSeekers': fs})



#FindOrderUI


#ConfirmOrderUI
def confirmOrder(request):
        orderManager=OrderManager()
        fp_id=request.session['fp_id']
        if request.method == 'POST' :
                confirm_order_id=request.POST.get("confirm_order_id")
                orderManager = OrderManager()
                orderManager.confirmOrder(fp_id, confirm_order_id)

        return redirect('confirmOrder')


#NegotiateOrderUI


#DeliverOrderUI

#AdressUI
'''def addAddressUI(request):
    #adressAttributeList=['building','street','landmark','city','state','country','pincode']
    address={}
    if request.method=="POST":
        address['building'] = request.POST.get('building') 
        address['street'] = request.POST.get('street')
        address['landmark'] = request.POST.get('landmark')
        address['city'] = request.POST.get('city')
        address['state'] = request.POST.get('state')
        address['country'] = request.POST.get('country')
        address['pincode'] = request.POST.get('pincode') 
    addressManager = AddressManager()
    addressManager.addAddress(address)
    addressList = addressManager.showAddresses()
    return render(request,'FoodServices/loadAddress.html',
    {
        'address':addressList,
    })

def deleteAddressUI(request):
    if request.method=="POST":
        id=request.POST.get("delete")
    return id


def editAddressUI(request):
    if request.method=="POST":
        id=request.POST.get("edit")
        
    return id

'''
#SigninUI
def displaySignInForm(request):
    return render(request,'raisemodifyorder/signin.html')

def displayFeedbackForm(request):
    pass

def displayFSOrderList(request):
    mobile_number = request.POST.get("mobile_number",False)
    modify_order_id =request.POST.get("order_id", False)
    modify_or_cancel=request.POST.get("modify_or_cancel",False)

    type_of_alert="sign_in"
    if(mobile_number == False and modify_order_id==False):
    	print('Coming from Raise Order')
    	mobile_number=request.session['mobile']
    	type_of_alert="raise_order"
    	submitOrderForm(request)

    elif(mobile_number==False):
    	print('Coming from modifyorder')
    	mobile_number=request.session['mobile']
    	if(modify_or_cancel=="modify"):
    		type_of_alert="modify_order"
    	else:
    		type_of_alert="cancel_order"
    	submitModifyOrderForm(request, modify_order_id, modify_or_cancel)


    print('Coming from Signin')
    request.session['mobile']=mobile_number
    loginManager= LoginManager()
    fs= loginManager.verifyUser(mobile_number)
    request.session['fs_id']=fs[0].fs_id
    orderManager=OrderManager()
    orders=orderManager.findOrders('food seeker', request.session['fs_id'])

    return render(request, 'raisemodifyorder/dashboard_foodseeker.html',{'FoodSeekers': fs, 'Orders': orders, "type_of_alert":type_of_alert})
 

def displayFPOrderList(request):
    pass

#SingUpUI
def displaySignUpForm():
    pass



def header(request):
	loginManager= LoginManager()
	fs= loginManager.verifyUser(request.session['mobile'])
    
	return render(request, 'raisemodifyorder/header.html',{'FoodSeekers': fs})




