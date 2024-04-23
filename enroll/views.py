from django.shortcuts import render, HttpResponseRedirect
from enroll.models import User
from enroll.forms import StudentRegistrationForm
# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistrationForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            psw = fm.cleaned_data['password']

            reg = User(name= nm, email = em, password = psw)
            reg.save()
            fm = StudentRegistrationForm()
    else:
        fm = StudentRegistrationForm()
    stud = User.objects.all()
    return render(request, 'enroll/addAndShow.html', {'form':fm, 'stu':stud})

def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistrationForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()  
        else:
            pi = User.objects.get(pk=id)
            fm = StudentRegistrationForm(instance=pi)   
             

    return render(request, 'enroll/updateStudent.html', {'form':fm})
