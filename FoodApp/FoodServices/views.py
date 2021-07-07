from django.shortcuts import render,redirect
from FoodServices import AddressManager
#RaiseOrderUI


#ModifyOrderUI


#FindOrderUI


#ConfirmOrderUI



#NegotiateOrderUI


#DeliverOrderUI

#AdressUI
def addAddressUI(request):
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

#SigninUI
def displayform(request):
    pass

def displayFeedbackForm(request):
    pass

def displayFSOrderList(request):
    pass

def displayFPOrderList(request):
    pass

#SingUpUI
def displaySignUpForm():
    pass




