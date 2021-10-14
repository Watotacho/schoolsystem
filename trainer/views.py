from .models import trainer
from django import forms
from django.forms.forms import Form
from django.shortcuts import redirect, render
from .forms import TrainerRegistrationForm


def register_trainer(request):
    if request.method=="POST":
      form=TrainerRegistrationForm(request.POST,request.FILES)
      if form.is_valid():
            form.save()
      else:
            print(form.errors)
    else:
        form=TrainerRegistrationForm()
    return render(request,"register_trainer.html",{"form":form})


def trainer_list(request):
    trainers=trainer.objects.all()
    return render(request,"trainer_list.html",{"trainers":trainers})

def edit_trainer(request,id):
    trainers=trainer.objects.get(id=id)
    if request.method=="POST":
        form=TrainerRegistrationForm(request.POST,instance=trainers)
        if form.is_valid():
            form.save()
    else:
        form=TrainerRegistrationForm(instance=trainers)
    return render(request,"edit_trainer.html",{"form":form})


def trainer_profile(request,id):
    trainers=trainer.objects.get(id=id)
    return render(request,"trainer_profile.html",{"trainer":trainers})


def delete_trainer(request,id):
    trainers=trainer.objects.get(id=id)
    trainers.delete()
    return redirect("trainer_list")




# Create your views here.
