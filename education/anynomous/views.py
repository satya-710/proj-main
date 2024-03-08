from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import test_employee


# Create your views here.s
def testprops(request):
     employees=test_employee.objects.all()
     context={
          'employees':employees
     }
     return render(request,'testprops.html',context)


def index (request):
    return render(request,'index.html')
def header (request):
    return render(request,'header.html')
def footer (request):
    return render(request,'footer.html')
def base (request):
    return render(request,'base.html')
def homepage (request):
    return render(request,'homepage.html')
def features (request):
    return render(request,'features.html')

def experties(request):
    return render(request,'experties.html')

def contactus(request):
	return render(request,'contactus.html')

def gallery(request):
     return render(request,'gallery.html') 

def login(request):
     return render(request,'login.html')

def signup(request):
     return render(request,'signup.html')

def testprops(request):
     return render(request,'testprops.html')
