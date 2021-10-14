from datetime import date


from django.shortcuts import render
from student.models import Student
from trainer.models import trainer
from course.models import Course
from events.models import Events




def home(request):
    students=Student.objects.count()
    trainers=trainer.objects.count()
    courses=Course.objects.count()
    events = Events.objects.count()

    data={"Student":students,"trainers":trainers,"courses":courses,"Events":events}
    return render(request,"home.html", data)

