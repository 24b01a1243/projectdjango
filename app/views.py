from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import StudentForm

def register_student(request):
    if request.method =='POST':
        form=StudentForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request,"Student registered successfully")
            return redirect('register_student')
        
        else:
            messages.error(request,"Please fix the errors below")
    else:
        form=StudentForm()
    return render(request,'register.html',{'form': form})



