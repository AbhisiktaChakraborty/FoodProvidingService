from django.contrib import admin
from django.urls import path
from FoodServices import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.addAddressUI,name="loadAddress"),
    path('signUp/',views.displaySignUpForm,name="signUp"),
    path('verifyUser/',views.verifyUserUI,name="verifyUser"),
    path('signin/',views.displayform,name="signin"),
    path('dashboardFoodSeeker/',views.displayFeedbackForm,name="dashboardFoodSeeker"),
    path('dashboardFoodProvider/',views.displayFPOrderList,name="dashboardFoodProvider")
]
