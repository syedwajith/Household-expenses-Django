# Generated by Django 4.0.7 on 2023-04-11 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HouseholdExpenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('House_Rent', models.FloatField()),
                ('Milk', models.FloatField()),
                ('Ration', models.FloatField()),
                ('Cable', models.FloatField()),
                ('Sandha', models.FloatField()),
                ('Grocery', models.FloatField()),
                ('Cylinder', models.FloatField()),
                ('Current_Bill', models.FloatField()),
                ('Total_salary', models.FloatField()),
                ('Total_Expenses', models.FloatField()),
                ('Balance_Amount', models.FloatField()),
                ('Date', models.DateField()),
            ],
        ),
    ]
