from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    tasks = Task.objects.all() #grabs all the information from the model for displaying on webpage

    form = TaskForm()#imports default form from forms.py file

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/lists.html', context)


#for updating the task
def updateTask(request, pk):
    task = Task.objects.get(id=pk)#for getting the info, needs to have a url in urls.py
    
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    
    return render(request, 'tasks/update_task.html', context) 

#for deleting the task
def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'tasks/delete.html', context)