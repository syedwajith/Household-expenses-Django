from django.shortcuts import render,redirect
from django.contrib import messages
from household_expenses_app.models import HouseholdExpenses
from household_expenses_app.forms import HouseholdExpensesForm

# Create your views here.

def index(request):
    return render(request, 'household_expenses_app/index.html')

def add_expenses(request):
    data = HouseholdExpenses()
    form = HouseholdExpensesForm
    if request.method == 'POST':
        form = HouseholdExpensesForm(request.POST)
        if form.is_valid():
            House_Rent = form.cleaned_data['House_Rent']
            Milk = form.cleaned_data['Milk']
            Ration = form.cleaned_data['Ration']
            Cable = form.cleaned_data['Cable']
            Sandha = form.cleaned_data['Sandha']
            Grocery = form.cleaned_data['Grocery']
            Cylinder = form.cleaned_data['Cylinder']
            Current_Bill = form.cleaned_data['Current_Bill']
            Total_salary = form.cleaned_data['Total_salary']
            Date = form.cleaned_data['Date']
            data.House_Rent = House_Rent
            data.Milk = Milk
            data.Ration = Ration
            data.Cable = Cable
            data.Sandha = Sandha
            data.Grocery = Grocery
            data.Cylinder = Cylinder
            data.Current_Bill = Current_Bill
            data.Total_salary = Total_salary
            data.Date = Date
            total_expenses = House_Rent + Milk + Ration + Cable + Sandha + Grocery + Cylinder + Current_Bill
            data.Total_Expenses = total_expenses
            data.Balance_Amount = Total_salary - total_expenses
            data.save()
            messages.success(request, 'Datas are saved successfully')
            return redirect('/household_expenses_app/add_expenses')
    return render(request, 'household_expenses_app/addexpenses.html', {'form':form})

def view_expenses(request):
    expenses_details = HouseholdExpenses.objects.all()
    if expenses_details.exists():
        return render(request, 'household_expenses_app/viewexpenses.html', {'expenses_details':expenses_details})
    else:
        messages.error(request, 'No results found')
    return render(request, 'household_expenses_app/viewexpenses.html')