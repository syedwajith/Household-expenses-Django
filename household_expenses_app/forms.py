from django import forms
from household_expenses_app.models import HouseholdExpenses

class HouseholdExpensesForm(forms.ModelForm):
    class Meta:
        model = HouseholdExpenses
        fields = ['House_Rent','Milk','Ration','Cable','Sandha','Grocery','Cylinder','Current_Bill','Total_salary','Date']
        widgets = {
            'Date': forms.DateInput(attrs={'class': 'date-feild'}),
        }