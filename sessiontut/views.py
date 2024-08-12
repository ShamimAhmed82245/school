from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def set(request):
    request.session['name']={'nam1':'simar','nam2':'rahul'}
    request.session['fatherName'] = 'john'
    # request.session.set_expiry(5)
    return HttpResponse("hello")

def get(request):
    name = request.session['name']
    fatherName = request.session['fatherName']
    print(name)
    print(fatherName)
    return HttpResponse(f"<h1>get view</h1> {name}")
    
def delete(request):
    # request.session.flush()
    request.session.clear_expired()
    # del request.session['name']
    return HttpResponse("<h1>delete view</h1>")

def update(request):
    request.session['name']['nam1']='john'
    request.session.modified=True
    return HttpResponse("<h1>update view</h1>")