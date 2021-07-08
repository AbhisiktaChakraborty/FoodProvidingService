from django.contrib import admin
from .models import Address,Order,FoodProvider,FoodSeeker,Messages
# Register your models here.
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(FoodProvider)
admin.site.register(FoodSeeker)
admin.site.register(Messages)