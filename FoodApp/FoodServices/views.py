from django.shortcuts import render,redirect
from FoodServices.AddressManager import AddressManager
from FoodServices.LoginManager import LoginManager
from FoodServices.OrderManager import OrderManager
#RaiseOrderUI


#ModifyOrderUI


#FindOrderUI


#ConfirmOrderUI



#NegotiateOrderUI


#DeliverOrderUI

#AdressUI
def showAddressUI(request):
    address=[]
    addressManager = AddressManager() 
    addressList=addressManager.showAddresses()
    if request.method=="POST":
        edit_id=request.POST.get("edit")
        delete_id=request.POST.get("delete")
        if edit_id is not None:
            print("Edit Address")
            add_obj=addressManager.findAddressObject(edit_id)
            print(add_obj)
            request.session['add_obj_edit']=add_obj
            return redirect('editAddress')
        elif delete_id is not None:
            addressManager.deleteAddress(delete_id)
            return render(request,'FoodServices/loadAddress.html',
    {
        'addressList':addressList,
    })
    return render(request,'FoodServices/loadAddress.html',
    {
        'addressList':addressList,
    })

def addAddressUI(request):
    addressManager=AddressManager()
    address=[]
    if request.method=="POST":
        address.append(request.POST.get('building'))
        address.append(request.POST.get('street'))
        address.append(request.POST.get('landmark'))
        address.append(request.POST.get('city'))
        address.append(request.POST.get('state'))
        address.append(request.POST.get('country'))
        address.append(request.POST.get('pincode'))

        addressManager.addAddress(address) 

        return redirect('loadAddress')

    return render(request,'FoodServices/addAddress.html')



def editAddress(request):
    addressManager=AddressManager()
    address=[]
    add_obj=request.session['add_obj_edit']
    print(add_obj)
    print("Edit Outside Funtion")
    if request.method=="POST":
        print("Edit Address UI")
        id=request.POST.get('add_id')
        address.append(request.POST.get('add_id'))
        address.append(request.POST.get('building'))
        address.append(request.POST.get('street'))
        address.append(request.POST.get('landmark'))
        address.append(request.POST.get('city'))
        address.append(request.POST.get('state'))
        address.append(request.POST.get('country'))
        address.append(request.POST.get('pincode'))
        
        addressManager.editaddress(address)

        return redirect('loadAddress')

    return render(request,'FoodServices/editAddress.html',
    {
        'add_obj':add_obj,
    })

#SigninUI
def displayform(request):
    print("Hello")
    result=0
    if request.method=="POST":
        mobile_number=request.POST.get("mobile-number")
        user_role=request.POST.get("UserType")
        loginManager = LoginManager()
        result = loginManager.verifyUser(mobile_number,user_role)
        print(result)
        if result[0]==1:
            print("User is Registered Food Provider")
            request.session['user_type']="FoodProvider"
            request.session['user_id']=result[1]
            return redirect('verifyUser')
        elif result[0]==2:
            print("User is registered Food Seeker")
            request.session['user_type']="FoodSeeker"
            request.session['user_id']=result[1]
            return redirect('verifyUser')
        else:
            print("User is Not Registered!")
            return render(request,'FoodServices/signIn.html',{'result':result})
    return render(request,'FoodServices/signin.html',{'result':result})


def displayFeedbackForm(request):
    loginManager=LoginManager()
    if request.method=="POST":
        rating=request.POST.get("rating")
        loginManager.getFeedback(rating,request.session['user_id'])
        return redirect('dashboardFoodSeeker')
    return render(request,'FoodServices/feedbackForm.html')

def displayFSOrderList(request):
    id=request.session['user_id']
    user_type=request.session['user_type']
    orderManager=OrderManager()
    orderDetails=orderManager.fetchOrderDetails(id,user_type)
    return render(request,'FoodServices/dashboardFoodSeeker.html',
    {
        'orderList':orderDetails,
    })


def displayFPOrderList(request):
    id=request.session['user_id']
    user_type=request.session['user_type']
    orderManager=OrderManager()
    orderDetails=orderManager.fetchOrderDetails(id,user_type)
    for orders in orderDetails:
        print(orders.order_id)
    return render(request,'FoodServices/dashboardFoodProvider.html',
    {
        'orderList':orderDetails,
    })
def verifyUserUI(request):
    otp=0
    if request.method=="POST":
        otp=request.POST.get("otp")
    loginManager=LoginManager()
    print(otp)
    result = loginManager.getOTP(otp)
    
    if request.session['user_type']=="FoodSeeker" and result>0:
        delivered_orders = loginManager.checkPreviousOrders(request.session['user_id'])
        print(delivered_orders)
        if delivered_orders==0:
            return redirect('dashboardFoodSeeker')
        elif delivered_orders==1:
            print("Feedback Form")
            return redirect('feedbackForm')
    elif request.session['user_type']=="FoodProvider" and result>0:
        return redirect('dashboardFoodProvider')
    return render(request,'FoodServices/verifyUser.html')
    
#SingUpUI
def displaySignUpForm(request):
    FP={}
    FS = {}
    result=[99]
    loginManager=LoginManager()
    if request.method=="POST":
        mobile=request.POST.get("mobile-number")
        if request.POST.get("UserType")=="FoodProvider":
            print("Food Provider")
            FP['mobile-number']=request.POST.get("mobile-number")
            FP['name']=request.POST.get("name")
            FP['email']=request.POST.get("email")
            FP['role']="FoodProvider"
            #login Manager
            result = loginManager.addNewUser(FP)
            print(result)
            
        elif request.POST.get("UserType")=="FoodSeeker":
            print("Food Seeker")
            FS['mobile-number']=request.POST.get("mobile-number")
            FS['name']=request.POST.get("name")
            FS['email']=request.POST.get("email")
            FS['role']="FoodSeeker"
            result = loginManager.addNewUser(FS)
            print(result)
    
    if result[0]==0:
        return render(request,'FoodServices/verifyUser.html')

    elif result[0]==1:
        request.session['user_type']="FoodProvider"
        request.session['user_id']=result[1]
        return render(request,'FoodServices/signUp.html',
        {
            'result':1
        })
    elif result[0]==2:
        request.session['user_type']="FoodSeeker"
        request.sesstion['user_id']=result[1]
        return render(request,'FoodServices/signUp.html',{
            'result':1
        })
    else:
        return render(request,'FoodServices/signUp.html',{
            'result':0
        })
    




