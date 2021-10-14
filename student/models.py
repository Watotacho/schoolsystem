# from _typeshed import self
from datetime import datetime
from django.db import models
class Student(models.Model):
    def test_year_of_birth(self):
        current_year=datetime.datetime.now().year
        year=current_year-self.student.age
        self.assertEqual(year,self.student.year_of_birth)
    first_name=models.CharField(max_length=12,default=30,null=True)
    last_name=models.CharField(max_length=10,default=20,null=True)
    age=models.PositiveSmallIntegerField()
    nations = [
        ("Kenyan","KENYAN"),
        ("Ugandan","UGANDAN"),
        ("Rwandan","RWANDAN"),
        ("South Sudan","SOUTH SUDAN")
    ]
    nationality=models.CharField(max_length=15,choices=nations,default="Kenyan")

    guardian_email=models.EmailField()
    guardian_name=models.CharField(max_length=12,default=20,null=True,blank=True)
    admission_date=models.DateField()
    image=models.ImageField(upload_to="images/",null=True)


    phone_number=models.CharField(max_length=12,default=30,null=True)
    guardian_phone_number=models.CharField(max_length=12,default=30,null=True)
    class_name=models.CharField(max_length=12,default=20,null=True)

    gender = [
        ("Female","FEMALE"),
        ("Male","MALE"),
        ("Others","OTHERS"),

    ]
    gender=models.CharField(max_length=15,choices=gender,default="Female")

    language = [
        ("English","ENGLISH"),
        ("Swahili","SWAHILI"),

    ]
    language=models.CharField(max_length=15,choices=language,default="English")


    academic_year=models.IntegerField(default=0)

def full_name(self):
    return f"{self.first_name} {self.last_name}"






# Create your models here.
