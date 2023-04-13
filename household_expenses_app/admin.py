from django.contrib import admin
from household_expenses_app.models import HouseholdExpenses

# Register your models here.

class HouseholdExpensesAdmin(admin.ModelAdmin):
    list = ['House_Rent','Milk','Ration','Cable','Sandha','Grocery','Cylinder','Current_Bill','Total_salary','Balance_Amount','Date']

admin.site.register(HouseholdExpenses,HouseholdExpensesAdmin)