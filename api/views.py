from django.shortcuts import render

from rest_framework import serializers, viewsets

from student.models import Student
from trainer.models import trainer
from course.models import Course
from events.models import Events

from .serializers import StudentSerializer
from .serializers import TrainerSerializer
from .serializers import CourseSerializer
from .serializers import EventsSerializer


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = trainer.objects.all()
    serializer_class=TrainerSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class=CourseSerializer

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class =EventsSerializer


