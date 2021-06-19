from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

def HomePage(request):
    #return HttpResponse('<h1>Hello Robinoud</h1>')
    return render(request, 'school/home.html')

def AboutPage(request):
    return render(request, 'school/about.html')

def ContactUs(request):
    return render(request, 'school/contactus.html')