from django.db import models

# Create your models here.

class HouseholdExpenses(models.Model):
    House_Rent = models.FloatField()
    Milk = models.FloatField()
    Ration = models.FloatField()
    Cable = models.FloatField()
    Sandha = models.FloatField()
    Grocery = models.FloatField()
    Cylinder = models.FloatField()
    Current_Bill = models.FloatField()
    Total_salary = models.FloatField()
    Total_Expenses = models.FloatField()
    Balance_Amount = models.FloatField()
    Date = models.DateField()