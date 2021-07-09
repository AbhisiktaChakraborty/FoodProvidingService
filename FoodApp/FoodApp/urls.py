from django.contrib import admin
from django.urls import path
from FoodServices import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showAddressUI,name="loadAddress"),
    path('addAddress/',views.addAddressUI,name="addAddress"),
    path('editAddress/',views.editAddress,name="editAddress"),
    path('signUp/',views.displaySignUpForm,name="signUp"),
    path('verifyUser/',views.verifyUserUI,name="verifyUser"),
    path('signin/',views.displayform,name="signin"),
    path('feedbackForm/',views.displayFeedbackForm,name="feedbackForm"),
    path('dashboardFoodProvider/',views.displayFPOrderList,name="dashboardFoodProvider"),
    path('dashboardFoodSeeker/',views.displayFSOrderList,name="dashboardFoodSeeker")
]
