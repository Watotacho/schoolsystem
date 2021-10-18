from django.db import models

class trainer(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=10)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
    phone_number=models.CharField(max_length=12)
    resume=models.FileField()
    course_name=models.CharField(max_length=15)
    email=models.CharField(max_length=12)
    city=models.CharField(max_length=10)
    salary=models.BigIntegerField()
    company_name=models.CharField(max_length=12)
    image=models.ImageField(upload_to="images/",null=True)


# Create your models here.
