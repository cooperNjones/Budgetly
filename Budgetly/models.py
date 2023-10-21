from django.db import models

# Create your models here.

class AccountInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=12)
class BudgetInfo(models.Model):
    user_budget = models.IntegerField()
    date = models.DateTimeField()
    description = models.CharField(max_length=100)
    label = models.CharField(max_length=10)
    Amount = models.DecimalField(max_digits=6, decimal_places=2)
    title = models.CharField(max_length=50)
    expenses = models.IntegerField()
    category = models.CharField(max_length=10)
    accountnumber = models.IntegerField()
    routingnumber = models.IntegerField()
    user = models.ForeignKey(AccountInfo, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    planned = models.DecimalField(max_digits=6, decimal_places=2)
    recieve = models.DecimalField(max_digits=6, decimal_places=2)