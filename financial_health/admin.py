from django.contrib import admin

# Registering models here.
from finance_future.models import FinancialHealth, UserInsights   #Need to add more models here

#Registering the models to make them available in the admin panel
admin.site.register(FinancialHealth)
admin.site.register(UserInsights)
