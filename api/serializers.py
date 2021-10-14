from rest_framework import serializers
from student.models import Student
from trainer.models import trainer
from course.models import Course
from events.models import Events


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=("first_name", "last_name","age")

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model=trainer
        fields=("first_name", "last_name","city")

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=("course_name", "course_code","course_channel")

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Events
        fields=("events")
