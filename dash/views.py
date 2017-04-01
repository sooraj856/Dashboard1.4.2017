from django.shortcuts import render, HttpResponse , render_to_response
from django.template import loader
from .models import task_item
from datetime import date , datetime

def index(request):
   
    if request.method == 'POST':
        task_item_obj1 = task_item(task_name='task_name', task_duration=60,
                                  task_project='task_project',task_priority='task_priority',
                                  task_status='hello',task_category='task_category')
        task_item_obj1.save()
       # project = Project.objects.get(title=offset)
        task_name = request.POST.get('task_name', '')
        task_duration = request.POST.get('task_duration', '')
        task_category = request.POST.get('task_category', '')
        task_project = request.POST.get('task_project', '')
        task_priority = request.POST.get('task_priority', '')
        
        task_item_obj = task_item(task_name=task_name, task_duration=task_duration,
                                  task_project=task_project,task_priority=task_priority,
                                  task_status='hello',task_category=task_category)
        task_item_obj.save()
    task_item_inst=task_item.objects.order_by('task_name')
    template = loader.get_template('dash/index.html')
    context = {
        'task_item_inst': task_item_inst,
    }
    
    return HttpResponse(template.render(context, request))
    

def todo(request):
    flag=request.POST.get('status_flag')
    task_id=request.POST.get('task_id' )
    if flag==1 and request.method == 'POST':
        task_status_change=request.POST.get('task_status_change')
        task_item_obj1=task_item.objects.filter(id=task_id)
        task_item_obj1.task_status=task_status_change
        task_item_obj1.save()

    
    if request.method == 'POST':
        
        task_name = request.POST.get('task_name')
        if task_name== '':
            task_name='test'
        task_duration = request.POST.get('task_duration')
        task_actual = request.POST.get('task_actual')
        task_category = request.POST.get('task_category')
        task_project = request.POST.get('task_project')
        task_priority = request.POST.get('task_priority')
        task_status = request.POST.get('task_status')
        task_note = request.POST.get('task_note')
        task_date = request.POST.get('task_date')
        if task_date== '':
            task_date=date.today()
        task_time = request.POST.get('task_time')
        if task_time== '':
            task_time=datetime.now()
        
        task_item_obj = task_item(task_name=task_name, task_duration=task_duration,
                                  task_actual=task_actual,task_project=task_project,task_priority=task_priority,
                                  task_status=task_status,task_category=task_category,task_time=task_time,task_date=task_date,task_note=task_note)

       
        task_item_obj.save(force_insert=True)
   
    dateEnd = date.today()
    task_item_inst_list=task_item.objects.filter(task_category='List').exclude(task_date__gt=dateEnd)    
    task_item_inst_email=task_item.objects.filter(task_category='Email').exclude(task_date__gt=dateEnd)
    task_item_inst_calls=task_item.objects.filter(task_category='Calls').exclude(task_date__gt=dateEnd)
    template = loader.get_template('dash/todo.html')
    context = {
        'task_item_inst_list': task_item_inst_list,
        'task_item_inst_email': task_item_inst_email,
        'task_item_inst_calls': task_item_inst_calls,
    }
    
    return HttpResponse(template.render(context, request))



def taskedit(request):
    getid = request.POST.get('id')
    task_item_edit_obj=task_item.objects.get(id=getid)
    flag=request.POST.get('flag')
    if request.method == 'POST':
        if flag == 1:
            task_status_change = request.POST.get('task_status_change')
            task_id=request.POST.get('task_id')
            task_item_status_obj=task_item.objects.get(id=24)
            task_item_status_obj.task_status=task_status_change
            task_item_status_obj.save(force_update=True)
                        
        task_name = request.POST.get('task_name_edit')
        task_duration = request.POST.get('task_duration_edit')
        task_actual = request.POST.get('task_actual_edit')
        task_category = request.POST.get('task_category_edit')
        task_project = request.POST.get('task_project_edit')
        task_priority = request.POST.get('task_priority_edit')
        task_status = request.POST.get('task_status_edit')
        task_note = request.POST.get('task_note_edit')
        task_date = request.POST.get('task_date_edit')
        task_time = request.POST.get('task_time_edit')
        if task_date== '':
            task_date=date.today()
        
        if task_time== '':
            task_time=datetime.now()
        
        task_item_edit_obj = task_item(id=getid, task_name=task_name, task_duration=task_duration,
                                  task_actual=task_actual,task_project=task_project,task_priority=task_priority,
                                  task_status=task_status,task_category=task_category,task_time=task_time,task_date=task_date,task_note=task_note)

       
        task_item_edit_obj.save(force_update=True)

        return HttpResponse('')




def statuschange(request):
    
    flag=request.POST.get('flag')
    if request.method == 'POST':
        task_status_change = request.POST.get('task_status_change')
        task_id=request.POST.get('task_id')
        task_item_status_obj=task_item.objects.get(id=task_id)
        task_item_status_obj.task_status=task_status_change
        task_item_status_obj.save(force_update=True)
        
              
                          
        

        return HttpResponse('')


def statuscompleted(request):
    
    task_id=request.POST.get('flag_completed')
    task_item_status_obj=task_item.objects.get(id=task_id)
    task_item_status_obj.delete()
    
    if request.method == 'POST':
        task_item_status_obj.delete()
        
            
              
                          
        

        return HttpResponse('')

