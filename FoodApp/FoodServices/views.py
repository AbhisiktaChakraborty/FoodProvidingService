from django.shortcuts import render,redirect
from FoodServices.AddressManager import AddressManager
from FoodServices.LoginManager import LoginManager

#RaiseOrderUI


#ModifyOrderUI


#FindOrderUI


#ConfirmOrderUI



#NegotiateOrderUI


#DeliverOrderUI

#AdressUI
def addAddressUI(request):
    #adressAttributeList=['building','street','landmark','city','state','country','pincode']
    address=[]
    addressList=[]
    addressManager = AddressManager() 
    addressList.append(addressManager.showAddresses())
    print(addressList)
    if request.method=="POST":
        address.append(request.POST.get('building'))
        address.append(request.POST.get('street'))
        address.append(request.POST.get('landmark'))
        address.append(request.POST.get('city'))
        address.append(request.POST.get('state'))
        address.append(request.POST.get('country'))
        address.append(request.POST.get('pincode'))


        addressManager = AddressManager()
        addressManager.addAddress(address)

        return render(request,'FoodServices/loadAddress.html',
        {
                        'addresssList':addressList,
            })

        
    return render(request,'FoodServices/loadAddress.html',
    {
        'addressList':addressList,
        'hello':"hello",
    })

def deleteAddressUI(request):
    if request.method=="POST":
        id=request.POST.get("delete")
    return render(request,'FoodServices/loadAddress.html',
    {
        'id':id,
    })


def editAddressUI(request):
    if request.method=="POST":
        id=request.POST.get("edit")
        
    return render(request,'FoodServices/loadAddress.html',
    {
        'id':id,
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
        print(mobile_number)
        print(user_role)
        if result==1:
            print("User is Registered Food Provider")
            #return render(request,'FoodServices/dashboardFoodProvider.html',{'result':result})
            return redirect('/verifyUser',
            {
                'result':result,
            })
        elif result==2:
            print("User is registered Food Seeker")
            return redirect('dashboardFoodSeeker',{'result':result})
        
        else:
            print("User is Not Registered!")
            return render(request,'FoodServices/signIn.html',{'result':result})
        
        


    return render(request,'FoodServices/signin.html',{'result':result})


def displayFeedbackForm(request):
    if request.method=="POST":
        rating=request.POST.get("rating")
        
    return render(request,'FoodServices/dashboardFoodSeeker.html')

def displayFSOrderList(request):
    pass

def displayFPOrderList(request):
    return render(request,'FoodServices/dashboardFoodProvider.html')

def verifyUserUI(request):
    otp=0
    if request.method=="POST":
        otp=request.POST.get("otp")
    loginManager=LoginManager()
    print(otp)
    result = loginManager.getOTP(otp)
    
    if result==2:
        return redirect('dashboardFoodSeeker')
    elif result==1:
        return redirect('dashboardFoodProvider')
    return render(request,'FoodServices/verifyUser.html')
    
#SingUpUI
def displaySignUpForm(request):
    FP={}
    FS = {}
    #result=0
    result=[]
    user_type=99
    loginManager=LoginManager()
    if request.method=="POST":
        mobile=request.POST.get("mobile-number")
        if request.POST.get("UserType")=="FoodProvider":
            print("Food Provider")
            FP['mobile-number']=request.POST.get("mobile-number")
            FP['name']=request.POST.get("name")
            FP['email']=request.POST.get("email")
            #FS['address']=request.POST.get("address")
            FP['role']="FoodProvider"
            result = loginManager.addNewUser(FP)
            print(result)
            #user_type=result[1]
            #user_id=result[0]
        else:
            print("Food Seeker")
            FS['mobile-number']=request.POST.get("mobile-number")
            FS['name']=request.POST.get("name")
            #FS['address']=request.POST.get("address")
            FS['email']=request.POST.get("email")
            FS['role']="FoodSeeker"
            result = loginManager.addNewUser(FS)
            print(result)
            user_type=result[1]
            user_id=result[0]
    
    if user_type==0:
        return render(request,'FoodServices/verifyUser.html',{
            'user_id':user_id,
            'user_type':user_type,
        })
    else:
        return render(request,'FoodServices/signUp.html',{
        'user_type': user_type,

    })
    




