from django.db import models


class Course(models.Model):
    course_name=models.CharField(max_length=12)
    course_code=models.CharField(max_length=6)
    trainer_id=models.CharField(max_length=6)
    description=models.CharField(max_length=15)
    syllabus=models.CharField(max_length=12)
    course_channel=models.CharField(max_length=15)


# Create your models here.
