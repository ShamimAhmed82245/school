from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Students
from .forms import StudentForm
from django.db.models import Q
from django.core.paginator import Paginator
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


def search(request):
    query = request.GET.get('query',None)
    page_number = request.GET.get('page',1)
    students = Students.objects.filter(Q(name__icontains=query)|
                                      Q(student_class__icontains=query)|
                                      Q(age__icontains=query))
    paginator = Paginator(students,2)
    page_obj = paginator.get_page(page_number)
    print(query)
    print(page_obj)
    return render(request,'students/search.html',{'students':page_obj,'query': query})