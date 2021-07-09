from django.test import TestCase
from django.urls import reverse, resolve
from FoodServices import views

class TestUrls(TestCase):
    
    def test_accesses_correct_pages(self):
        self.loadAddress_url=reverse('loadAddress')
        self.signUp_url=reverse('signUp')
        self.verifyUser_url=reverse('verifyUser')
        self.signin_url=reverse('signin')
        self.dashboardFoodSeeker_url=reverse('dashboardFoodSeeker')
        self.dashboardFoodProvider_url=reverse('dashboardFoodProvider')
        self.feedbackForm_url=reverse('feedbackForm')

        self.assertEquals(resolve(self.loadAddress_url).func, views.showAddressUI)
        self.assertEquals(resolve(self.signUp_url).func, views.displaySignUpForm)
        self.assertEquals(resolve(self.verifyUser_url).func, views.verifyUserUI)
        self.assertEquals(resolve(self.signin_url).func, views.displayform)
        self.assertEquals(resolve(self.dashboardFoodSeeker_url).func, views.displayFSOrderList)
        self.assertEquals(resolve(self.dashboardFoodProvider_url).func, views.displayFPOrderList)
    