from .models import FoodSeeker

class LoginManager:
    def verifyUser(self,mobile):
        #after verifying, if verified, return the FoodSeeker object found
        fs = FoodSeeker.objects.filter(phone_no=mobile)
        return fs
         

    def getOTP(self):
        pass
    def addNewUser(self):
        pass
    def getFeedback(self):
        pass