from django.test import TestCase
from FoodServices.models import Address,FoodProvider,FoodSeeker,Order
from FoodServices.LoginManager import LoginManager

class TestViews(TestCase):
    #Login Manager
    '''def test_addNewUser(self):
           #add new User
        user_add = FoodSeeker(name="Sherlock Holmes",mobile="9903194876",email="abcd@gmail.com")
        user_add.save()
        print()
        print(user_add.mobile)
        isPresent = 0
        loginManager = LoginManager()
        role=input("Enter role: ")
        mn = input("Enter mobile number: ")
        name = input("Enter name: ")

        if role == "FoodProvider":
            FP={'mobile-number':mn,'name':name,'email':'abcd@gmail.com','role' : role} 
            
            result = loginManager.addNewUser(FP) #calling add new User
            
            fp=FoodProvider.objects.all()
            for i in fp:
                if FP['mobile-number']==i.mobile:
                    isPresent=1
                    break
        else:
            FS={'mobile-number':mn,'name':name,'email':'abcd@gmail.com','role' : role} 
            result = loginManager.addNewUser(FS)
            fs=FoodSeeker.objects.all()
            for i in fs:
                if FS['mobile-number']==i.mobile:
                    isPresent=1
                    break
        print(isPresent)
        print(result[0])
        res=0
        if result[0] != 0:
            res=1
        self.assertEqual(isPresent, res, "FAIL")

    def test_getOTP(self):
        print("Enter OTP:")
        otp=input()
        loginManager = LoginManager()
        result = loginManager.getOTP(otp)
        print(int(len(otp)==6))
        print(result)
        self.assertEqual(result,int(len(otp)==6),"FAIL")

    def test_verifyUser(self):
        user_add = FoodSeeker(name="Sherlock Holmes",mobile="9903194876",email="abcd@gmail.com")
        user_add.save()
        print()
        print(user_add.mobile)
        isPresent = 0
        loginManager = LoginManager()
        role=input("Enter role: ")
        mn = input("Enter mobile number: ")
        name = "JI"

        if role == "FoodProvider":
            FP={'mobile-number':mn,'name':name,'email':'abcd@gmail.com','role' : role} 
            
            result = loginManager.verifyUser(mn,role) #calling add new User
            
            fp=FoodProvider.objects.all()
            for i in fp:
                if FP['mobile-number']==i.mobile:
                    isPresent=1
                    break
        else:
            FS={'mobile-number':mn,'name':name,'email':'abcd@gmail.com','role' : role} 
            result = loginManager.verifyUser(mn,role)
            fs=FoodSeeker.objects.all()
            for i in fs:
                if FS['mobile-number']==i.mobile:
                    isPresent=1
                    break
        print(isPresent)
        print(result[0])
        res=0
        if result[0] != 0:
            res=1
        self.assertEqual(isPresent, res, "FAIL")'''

    '''def test_checkPreviousOrders(self):
        fs_id = int(input("Enter Food Seeker ID: "))
        order = Order(veg_healthy=2,veg_ill=2,nonveg_healthy=3,nonveg_ill=0,allergies="None",delivery_address="Honolulu",status='3',food_seeker_id=2,food_provider_id=3)
        order.save()
        orders=Order.objects.all()
        c=0
        loginManager = LoginManager()
        res = loginManager.checkPreviousOrders(fs_id)
        for o in orders:
            if o.status=='3' and o.food_seeker_id==fs_id:
                c=1
        self.assertEqual(c,res,"FAIL")'''

    def test_getFeedback(self):
        fs_id = 1
        rating = int(input("Enter Food Provider's rating: "))
        order = Order(veg_healthy=2,veg_ill=2,nonveg_healthy=3,nonveg_ill=0,allergies="None",delivery_address="Honolulu",status='3',food_seeker_id=fs_id,food_provider_id=1)
        order.save()
        fs = FoodSeeker(name="Sherlock Holmes",mobile="9903194876",email="abcd@gmail.com")
        fs.save()
        fp = FoodProvider(name="Sherlock",mobile="9905194876",email="abcd@gmail.com")
        fp.save()
        loginManager = LoginManager()
        loginManager.getFeedback(rating,fs_id)
        fp_id = order.food_provider_id
        foodProvider=FoodProvider.objects.get(fp_id=fp_id)
        self.assertEqual(foodProvider.ratings, rating, "FAIL")



    

