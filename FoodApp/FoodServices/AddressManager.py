from .models import Address
class AddressManager:

    def addAddress(self,address):

        addressObject = Address() #create Address object of Address Model
        print(address)

        #setting data
        addressObject.building =  address[0]
        addressObject.street = address[1]
        addressObject.landmark = address[2]
        addressObject.city = address[3]
        addressObject.state = address[4]
        addressObject.country = address[5]
        addressObject.pincode = address[6]

        #saving Model
        addressObject.save()

    def findAddressObject(self, id):
        address = Address.objects.get(add_id=id)
        addressList=[]
        addressList.append(address.add_id)
        addressList.append(address.building)
        addressList.append(address.street)
        addressList.append(address.landmark)
        addressList.append(address.city)
        addressList.append(address.state)
        addressList.append(address.country)
        addressList.append(address.pincode)
        return addressList


    def editaddress(self,address):
        print(address)
        addressObject = Address.objects.get(add_id=address[0])
        addressObject.building =  address[1]
        addressObject.street = address[2]
        addressObject.landmark = address[3]
        addressObject.city = address[4]
        addressObject.state = address[5]
        addressObject.country = address[6]
        addressObject.pincode = address[7]

        addressObject.save()

    def deleteAddress(self,id):
        print(id)
        address=Address.objects.get(add_id = id)
        address.delete()

    def showAddresses(self):
        addressObjects = Address.objects.all()
        #for i in addressObjects:
          #  print(i.add_id)
        return addressObjects

