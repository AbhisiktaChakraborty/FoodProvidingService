from FoodServices.models import FoodProvider,FoodSeeker

class LoginManager:


    def verifyUser(self,mobile,role):
        print("User Mobile")
        print(role)
        print(mobile)
        if role=="FoodProvider":
            fp=FoodProvider.objects.all()
            for i in fp:
                print("Food Provider Mobile")
                print(i.mobile)
                if i.mobile==mobile:
                    return 1 #user is registered food provider
        else:
            fs=FoodSeeker.objects.all()
            for i in fs:
                if i.mobile==mobile:
                    return 2 #user is registered food seeker
        return 0 #user is not registered


    def getOTP(self,otp):
        if len(str(otp))==6:
            return 1

        return 0

    def addNewUser(self,User):
        #print(User['role'])
        #print(User['name'])
        user_type=0
        if User['role']=="FoodProvider":
            #print("Food Provider DB")
            fp=FoodProvider.objects.all()
            print(User)
            for i in fp:
                #print(i.name)
                #print(i.mobile)
                if User['mobile-number']==i.mobile:
                    return 1 #food provider already exists
            
            #creating new food provider
            fp_new=FoodProvider()

            fp_new.name=User['name']
            #fp_new.address=User['address']
            fp_new.mobile=User['mobile-number']
            fp_new.email=User['email']

            fp_new.save()

            user_id=fp_new.fp_id
            user_type=1
        else:
            print("Food Seeker - DB")
            fs=FoodSeeker.objects.all()
            for i in fs:
                if User['mobile-number']==i.mobile:
                    return 2 #food seeker already exists
            
            #creating new food seeker
            fs_new=FoodSeeker()

            fs_new.name=User['name']
            #fs_new.address=User['address']
            fs_new.mobile=User['mobile-number']
            fs_new.email=User['email']

            fs_new.save()

            user_id=fs_new.fs_id
            user_type=2
        #user_type=0
        result=[user_id,user_type]
        return result

    def getFeedback(self):
        #SAVE RATING FOR FOOD PROVIDER
        pass

    