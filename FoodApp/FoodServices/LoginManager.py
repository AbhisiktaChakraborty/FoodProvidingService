from FoodServices.models import FoodProvider,FoodSeeker,Order
class LoginManager:
    def verifyUser(self,mobile,role): #during sign In
        print("User Mobile")
        print(role)
        print(mobile)
        result=[0]
        if role=="FoodProvider":
            fp=FoodProvider.objects.all()
            for i in fp:
                print("Food Provider Mobile")
                print(i.mobile)
                if i.mobile==mobile:
                    result[0]=1
                    result.append(i.fp_id)
                    return result #user is registered food provider
        elif role=="FoodSeeker":
            fs=FoodSeeker.objects.all()
            for i in fs:
                if i.mobile==mobile:
                    result[0]=2
                    result.append(i.fs_id)
                    return result #user is registered food seeker
        return result #user is not registered


    def getOTP(self,otp):
        if len(str(otp))==6:
            return 1

        return 0

    def addNewUser(self,User):
        result=[0]
        if User['role']=="FoodProvider":
            fp=FoodProvider.objects.all()
            print(User)
            for i in fp:
                if User['mobile-number']==i.mobile:
                    result[0]=1
                    return result #food provider already exists
            
            #creating new food provider
            '''fp_new=FoodProvider()

            fp_new.name=User['name']
            fp_new.mobile=User['mobile-number']
            fp_new.email=User['email']

            fp_new.save()'''
            fp = FoodProvider()
            fp_new=fp.setDetails(User)

            user_id=fp_new.fp_id
            #user_type=1
        else:
            print("Food Seeker - DB")
            
            fs=FoodSeeker.objects.all()
            for i in fs:
                if User['mobile-number']==i.mobile:
                    result[0]=2
                    return result #food seeker already exists
            
            #creating new food seeker
            fs_new=FoodSeeker()

            fs_new.name=User['name']
            #fs_new.address=User['address']
            fs_new.mobile=User['mobile-number']
            fs_new.email=User['email']

            fs_new.save()

            user_id=fs_new.fs_id
            #user_type=2
        #user_type=0
        result.append(user_id)
        return result

    def checkPreviousOrders(self,fs_id):
        orders=Order.objects.all()
        c=0
        for o in orders:
            if o.status=='3' and o.food_seeker_id==fs_id:
                c=1
        return c

    def getFeedback(self,rating,fs_id):
        orders=Order.objects.get(food_seeker_id=fs_id,status=3)
        fp_id = orders.food_provider_id
        foodProvider=FoodProvider.objects.get(fp_id=fp_id)
        foodProvider.ratings=rating
        foodProvider.save()


        

    