from django.shortcuts import render, HttpResponse , render_to_response 
from django.template import loader
import xlrd
import pyexcel as pe
import pyexcel.ext.xls
import pyexcel.ext.xlsx
import pyexcel.ext.ods3
from pyexcel._compact import OrderedDict
from .models import Expense , Day , OtaRev
import datetime
from datetime import timedelta
import csv
from django.http import HttpResponse
from wsgiref.util import FileWrapper



    

def homepage(request):
    template = loader.get_template('signatureinn/homepage.html')
   
    return HttpResponse(template.render(request))

def calculatetotal(request):
    
    if request.method == 'POST':        
        new_ota_rev_entry1_db =request.POST.get('new_ota_rev_entry1',0)        
        dropdownMenu1_db =request.POST.get('dropdownMenu1')
        new_ota_rev_entry2_db =request.POST.get('new_ota_rev_entry2',0)
        dropdownMenu2_db =request.POST.get('dropdownMenu2')
        new_ota_rev_entry3_db =request.POST.get('new_ota_rev_entry3',0)
        dropdownMenu3_db =request.POST.get('dropdownMenu3')
        new_ota_rev_entry4_db =request.POST.get('new_ota_rev_entry4',0)
        dropdownMenu4_db =request.POST.get('dropdownMenu4')
        
        date_expense_db =request.POST.get('form_date_expense')        
        maintainence_expense_db =request.POST.get('form_maintainence_expense')
        maintainence_text_expense_db =request.POST.get('form_maintainence_text_expense')
        bills_expense_db =request.POST.get('form_bills_expense')
        bills_text_expense_db =request.POST.get('form_bills_text_expense')
        inventory_expense_db =request.POST.get('form_inventory_expense')
        inventory_text_expense_db =request.POST.get('form_inventory_text_expense')
        diesel_expense_db =request.POST.get('form_diesel_expense')        
        salary_expense_db =request.POST.get('form_salary_expense')
        salary_text_expense_db =request.POST.get('form_salary_text_expense')
        bulk_expense_db =request.POST.get('form_bulk_expense')
        bulk_text_expense_db =request.POST.get('form_bulk_text_expense')
        total_expense_db =request.POST.get('expense_amt')
       
        daily_total_day_db =request.POST.get('daily_total')        
        expense_day_db =request.POST.get('expense_amt')
        cash_day_db =request.POST.get('cash_entry')
        card_day_db =request.POST.get('card_entry')
        counter_day_db =request.POST.get('counter_entry')
        bank_day_db =request.POST.get('bank_entry')
        ota_revenue_day_db =request.POST.get('ota_rev')
        total_revenue_day_db =request.POST.get('total_rev_entry')
        act_revenue_day_db=request.POST.get('actual_rev_entry')
        day_obj = Day(daily_total_day = daily_total_day_db,
                     expense_day = expense_day_db,
                     cash_day = cash_day_db,
                     card_day = card_day_db,
                     counter_day = counter_day_db,
                     bank_day = bank_day_db,
                     ota_revenue_day = ota_revenue_day_db,
                     total_revenue_day = total_revenue_day_db,
                     act_revenue_day = act_revenue_day_db,
                     title_day='hello')
        day_obj.save(force_insert=True)
        expense_obj = Expense(date_expense = date_expense_db,
                     maintainence_expense = maintainence_expense_db,
                     maintainence_text_expense = maintainence_text_expense_db,
                     bills_expense = bills_expense_db,
                     bills_text_expense = bills_text_expense_db,
                     inventory_expense = inventory_expense_db,
                     inventory_text_expense = inventory_text_expense_db,
                     diesel_expense = diesel_expense_db,
                     salary_expense = salary_expense_db,
                     salary_text_expense = salary_text_expense_db,
                     bulk_expense = bulk_expense_db,
                     bulk_text_expense = bulk_text_expense_db,
                     total_expense = total_expense_db)
        expense_obj.save(force_insert=True)
        if new_ota_rev_entry1_db != 0 :
            
            otarev_obj1= OtaRev(ota_amt = new_ota_rev_entry1_db,
                            ota_category = dropdownMenu1_db,
                            total_ota_rev = ota_revenue_day_db)
            otarev_obj1.save(force_insert=True)
        if new_ota_rev_entry2_db != 0 :
            otarev_obj2= OtaRev(ota_amt = new_ota_rev_entry2_db,
                            ota_category = dropdownMenu2_db,
                            total_ota_rev = ota_revenue_day_db)
            otarev_obj2.save(force_insert=True)
        if new_ota_rev_entry3_db != 0 :
            otarev_obj3= OtaRev(ota_amt = new_ota_rev_entry3_db,
                            ota_category = dropdownMenu3_db,
                            total_ota_rev = ota_revenue_day_db)
            otarev_obj3.save(force_insert=True)
        if new_ota_rev_entry4_db != 0 :
            otarev_obj4= OtaRev(ota_amt = new_ota_rev_entry4_db,
                            ota_category = dropdownMenu4_db,
                            total_ota_rev = ota_revenue_day_db)
            otarev_obj4.save(force_insert=True)    
    return HttpResponse('')


def dailyacs(request):
    template = loader.get_template('signatureinn/dailyacs.html')

    return HttpResponse(template.render(request))
    


def dailyacsdata(request):
    
    total_expense=Expense.objects.order_by('id').reverse()[0].total_expense
    db_total_revenue_day=Day.objects.order_by('id').reverse()[0].total_revenue_day
    db_act_revenue_day=Day.objects.order_by('id').reverse()[0].act_revenue_day
    db_cash_total=Day.objects.order_by('id').reverse()[0].cash_day
    db_bank_total=Day.objects.order_by('id').reverse()[0].bank_day
    db_card_total=Day.objects.order_by('id').reverse()[0].card_day
    db_ota_rev_total=OtaRev.objects.order_by('id').reverse()[0].total_ota_rev
    flag=request.POST.get('flag',0) 
    
    ind=0
    x=0
    y=0
    invoice_num=[]
    advance_num=[]
    invoice_amt=[]
    advance_amt=[]
    day_test=26
    month_test=4
    
    if request.method == 'POST':
        
        day_test=int(request.POST.get('date_day1'))
        month_test=int(request.POST.get('date_month1'))
        
    
    response = HttpResponse()
    my_dict = pyexcel.get_dict(file_name="C:\Python27\day%d.%d.xls"%(day_test,month_test), name_columns_by_row=0)
    records = pe.get_records(file_name="C:\Python27\day%d.%d.xls"%(day_test,month_test), name_columns_by_row=0)
        
        
    for key, values in my_dict.items():
        
        if key=='invoice_num':
            for record in records:
                invoice_num.append({'num':record['invoice_num'],'amt':record['invoice_amt']})
                invoice_amt.append(record['invoice_amt'])
                x=x+1
        elif key=='advance_num':
            for record in records:
                if record['Company']!='x':
                    advance_num.append({'num':record['advance_num'],'amt':record['Company']})
                    advance_amt.append(record['Company'])
                        
                else:
                        
                    advance_num.append({'num':record['advance_num'],'amt':record['advance_amt']})
                    advance_amt.append(record['advance_amt'])
                y=y+1    
                    
    template = loader.get_template('signatureinn/dailyacsdata.html')        
    Expense_list = Expense.objects.all()   
    context = {               
        'invoice_num': invoice_num,
        'advance_num': advance_num,
        'invoice_amt': invoice_amt,
        'advance_amt': advance_amt,
        'adv_excel_counter': x,
        'inv_excel_counter': y,
        'Expense_list' : Expense_list,
        'total_expense': total_expense,
        'db_bank_total':db_bank_total,
        'db_cash_total':db_cash_total,
        'db_card_total':db_card_total,
        'db_ota_rev_total':db_ota_rev_total,
        'db_total_revenue_day':db_total_revenue_day,
        'db_act_revenue_day':db_act_revenue_day,
        
    }
    
        
    return HttpResponse(template.render(context, request))

    
    
 
def feedback(request): 
      
    my_dict = pyexcel.get_dict(file_name="C:\\Users\\admin\\Desktop\\review mail\\Feedback Tab\\feedback.xls", name_columns_by_row=0)
    records = pe.get_records(file_name="C:\\Users\\admin\\Desktop\\review mail\\Feedback Tab\\feedback.xls", name_columns_by_row=0)
    template = loader.get_template('signatureinn/feedback.html')
    
    ind=0
    xx=0
    
    
    fb_num=[]
    rm_num=[]
    fd_score=[]
    hk_score=[]
    total_score=[]
    d=datetime.datetime(2016, 6, 14, 12, 30)
    for record in records:       
        
        if record['Front Desk / Service']>=3 and record['Front Desk / Efficiency']>=3 and record['Front Desk / Welcome']>=3 and record['Housekeeping / Common Areas']>=3 and record['Date Time']>d:
            xx=xx+1 
            fb_num.append({'feedback':record['Feedback ID'],'room':record['Room No'],'date':record['Date Time']})
            rm_num.append({'feedback':record['Feedback ID'],'room':int(record['Room No']),'date':datetime.datetime.strptime(str(record['Date Time']),'%Y-%m-%d %H:%M:%S').date()})




    my_dict1 = pyexcel.get_dict(file_name="C:\\Users\\admin\\Desktop\\review mail\\Check Out\\dep18.7.xls", name_columns_by_row=3)
    records_winhms = pe.get_records(file_name="C:\\Users\\admin\\Desktop\\review mail\\Check Out\\dep18.7.xls", name_columns_by_row=3)
    
    
    
    yy=0
    zz=0
    wn_num=[]
    wn_rm_num1=[]
    fd_score=[]
    hk_score=[]
    total_score=[]
    for records in records_winhms:
        yy=yy+1
        date=str(records['Depart   Dt'])
        if date!="" :
            
            for value in rm_num:
                wn_rm_num1.insert(zz,{'room':value['room']})
                value1=str(value['room'])
                value2=datetime.datetime.strptime(date,'%d/%m/%y').date()
                if records['Room No']==value1 and value2==value['date']:
                        
                        zz=zz+1
                
                        wn_num.append({'room':records['Room No'],'date':records['Depart   Dt'],'email':records['E-Mail'],'name':records['Guest Name ']})
            
            
            
    filename = open('C:/Users/admin/Desktop/review mail/test.csv', 'w+')
    wrapper  = FileWrapper(filename)
    response = HttpResponse(wrapper , content_type='text/csv')
    response['Content-Disposition'] = "attachment; filename='test.csv'"

    writer = csv.writer(response)
    writer.writerow(['Room', 'Date', 'Name', 'Email'])
    for value in wn_num:
        
        writer.writerow([value['room'], value['date'],value['name'],value['email']])

    return response

        
    context = {
        'fb_num': fb_num,
        'rm_num': rm_num,
        'wn_num': wn_num,
        'room_count':xx,
        'wn_room_count':zz,
        }





    return HttpResponse(template.render(context, request))
