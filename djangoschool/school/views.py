from django.db.models.fields import EmailField
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .models import ExamScore, AllStudent, Profile


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

############################ Search Page ###################################
@login_required
def SearchStudent(request):
    # MODELS.object.all() ดึงค่ามาทั้งหมด
    # MODELS.object.get(student_id = '6300001') ดึงค่าแค่ตัวเดียว หากเกิน จะ error
    # MODELS.object.filter(level = 'ม.1') ดึงค่ามาหลายค่า
    if request.method == 'POST' and request.FILES['photoprofile']:
        data = request.POST.copy()
        searchid = data.get('search') 
        print(searchid, type(searchid))
        try:
            result = AllStudent.objects.get(student_id = searchid)
            print('RESULT', result)
            context = {'result':result,'check':'found'}
        except:
            context = {'result':'ไม่มีข้อมูลในระบบ','check':'notfound'}

        return render(request, 'school/search.html', context)

    return render(request, 'school/search.html')


############################ Edit Profile ###################################
@login_required
def EditProfile(request):

    username = request.user.username
    current = User.objects.get(username=username)


    if request.method == 'POST':
        data = request.POST.copy()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')

        myprofile = User.objects.get(username=username)
        try:
            setprofile = Profile.objects.get(user=myprofile)
        except:
            setprofile = Profile()
            setprofile.user = myprofile

        ####### file system ########
        file_image = request.FILES['photoprofile']
        file_image_name = file_image.name
        fs = FileSystemStorage()
        filename = fs.save(file_image_name, file_image)    
        upload_file_url = fs.url(filename)
        setprofile.photoprofile = upload_file_url[6:]
        setprofile.save()

        ####### 
        myprofile.username = email
        myprofile.first_name = first_name
        myprofile.last_name = last_name
        myprofile.email = email
        myprofile.save()


        # from django.shortcuts import redirect
        return redirect('editprofile-page')

    context = {'data':current}
    return render(request, 'school/editprofile.html',context)