from.models import Student
from .models import Student
from django import forms
from django.shortcuts import redirect, render
from .forms import StudentRegistrationForm


def register_student(request):
    if request.method=="POST":
        form=StudentRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=StudentRegistrationForm()
    return render(request,"register_student.html",{"form":form})


def student_list(request):
    students=Student.objects.all()
    return render(request,"student_list.html",{"students":students})


def edit_student(request,id):
    students=Student.objects.get(id=id)
    if request.method=="POST":
        form=StudentRegistrationForm(request.POST,instance=students)
        if form.is_valid():
            form.save()
    else:
        form=StudentRegistrationForm(instance=students)
    return render(request,"edit_student.html",{"form":form})


def student_profile(request,id):
    students=Student.objects.get(id=id)
    return render(request,"student_profile.html",{"student":students})


def delete_student(request,id):
    students=Student.objects.get(id=id)
    students.delete()
    return redirect("student_list")

