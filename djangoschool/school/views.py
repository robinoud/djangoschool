from django.db.models.fields import EmailField
from django.shortcuts import render, redirect
from .models import ExamScore
from django.contrib.auth.models import User
#from django.http import HttpResponse
# Create your views here.

def HomePage(request):
    #return HttpResponse('<h1>Hello Robinoud</h1>')
    return render(request, 'school/home.html')

def AboutPage(request):
    return render(request, 'school/about.html')

def ContactUs(request):
    return render(request, 'school/contactus.html')

def ShowScore(request):
    score = ExamScore.objects.all() # ดึงค่า จาก DB มาทั้งหมด

    context = {'score' : score}

    return render(request, 'school/showscore.html', context)

def Register(request):

    if request.method == 'POST':
        data = request.POST.copy()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')

        newuser = User()
        newuser.username = email
        newuser.first_name = first_name
        newuser.last_name = last_name
        newuser.email = email
        newuser.set_password(password)
        newuser.save()
        # from django.shortcuts import redirect
        return redirect('home-page')

    return render(request, 'school/register.html')