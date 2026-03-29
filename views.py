from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .forms import Taskform

def index(request):
    tasks=Task.objects.all().order_by('-created')
    form=Taskform( )

    if request.method =='POST':
        form=Taskform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')    
    context={'tasks':tasks,'form':form}
    return render(request,'index.html',context)
#update task
def update_task(request,id):
    tasks=get_object_or_404(Task,id=id)
    form=Taskform(instance=tasks)
    if form.is_valid():
            form.save()
            return redirect('/')    
    context={'tasks':tasks,'form':form}
    return render(request,'update.html',context)

#delete
def delete_task(request,id):
     tasks=Task.objects.get(id=id)
     tasks.delete()
     return redirect('/')

    #create 
    #def create_task(request)
        # if request.method=='POST'
        #task.objects.create(title=request.post['title'])
        #return redirect('/')
        #return render(request,'index.html')