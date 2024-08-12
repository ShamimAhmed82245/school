from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Students
from .forms import StudentForm
# Create your views here.


def home(request):
    students=Students.objects.all()
    return render(request,'students/home.html',{'students':students})

def add(request):
    if request.method=='POST':
        form =  StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/student/home/')
    else:  
        form = StudentForm()
    return render(request, 'students/add-student.html',{'form':form})

def update(request,id):
    student = Students.objects.get(id=id)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/student/home/')
    else:
        form=StudentForm(instance=student)
    return render(request,'students/update.html',{'form':form})