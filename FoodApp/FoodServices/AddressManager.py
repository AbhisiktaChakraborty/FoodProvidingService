from .models import Address
class AddressManager:

    def addAddress(self,address):

        addressObject = Address() #create Address object of Address Model
        print(address)

        #setting data
        addressObject.building =  address['building']
        addressObject.street = address['street']
        addressObject.landmark = address['landmark']
        addressObject.city = address['city']
        addressObject.state = address['state']
        addressObject.country = address['country']
        addressObject.pincode = address['pincode']

        #saving Model
        addressObject.save()



    def editaddress(self,id):
        pass

    def deleteAddress(self,id):
        
        address=Address.objects.get(add_id = id)
        address.delete()

    def showAddresses(self):
        addressObjects = Address.objects.all()
        return addressObjects

