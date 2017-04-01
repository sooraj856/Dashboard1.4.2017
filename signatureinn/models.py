from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.


class Day(models.Model):    
    daily_total_day = models.IntegerField(null=True,blank=True)
    expense_day = models.IntegerField(null=True,blank=True)
    title_day = models.CharField(max_length=50,null=True,blank=True)
    cash_day = models.IntegerField(null=True,blank=True)
    card_day = models.IntegerField(null=True,blank=True)
    counter_day = models.IntegerField(null=True,blank=True)
    bank_day = models.IntegerField(null=True,blank=True)
    ota_revenue_day = models.IntegerField(null=True,blank=True)
    total_revenue_day = models.IntegerField(null=True,blank=True)
    act_revenue_day = models.IntegerField(null=True,blank=True)
    
    def __str__(self):              
        return str(self.title_day)



class Expense(models.Model):
    date_expense = models.DateField(null=True,blank=True)
    maintainence_expense = models.IntegerField(null=True,blank=True)
    maintainence_text_expense = models.CharField(max_length=50,null=True,blank=True)
    bills_expense = models.IntegerField(null=True,blank=True)
    bills_text_expense = models.CharField(max_length=50,null=True,blank=True)
    inventory_expense = models.IntegerField(null=True,blank=True)
    inventory_text_expense = models.CharField(max_length=50,null=True,blank=True)
    diesel_expense = models.IntegerField(null=True,blank=True)
    salary_expense = models.IntegerField(null=True,blank=True)
    salary_text_expense = models.CharField(max_length=50,null=True,blank=True)
    bulk_expense = models.IntegerField(null=True,blank=True)
    bulk_text_expense = models.CharField(max_length=50,null=True,blank=True)
    total_expense = models.IntegerField(null=True,blank=True)
    
        
    def __str__(self):              
        return self.maintainence_text_expense





class OtaRev(models.Model):
    ota_amt = models.IntegerField(null=True,blank=True)
    ota_category = models.CharField(max_length=50,null=True,blank=True)
    total_ota_rev = models.IntegerField(null=True,blank=True)


    def __str__(self):              
        return str(self.ota_category)
    

