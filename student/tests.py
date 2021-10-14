from datetime import datetime
from django.test import TestCase
from logging import currentframe
from django import urls
from django.http import request
from .models import Student
import datetime
from django .urls import reverse

class StudentModelTestCase(TestCase):
    def setUp(self):
        self.student=Student(first_name="James",
                             last_name="Daniel",
                             age=24,
                             gender="Male"
        ),
    def test_full_name_contains_first_name(self):
        self.assertIn(self.student.first_name,self.student.last_name())

    def test_full_name_contains_last_name(self):
        self.assertIn(self.student.last_name,self.student.full_name())

    def test_year_of_birth(self):
        current_year=datetime.datetime.now().year
        year=current_year-self.student.age
        self.assertEqual(year,self.student.year_of_birth())

    def test_student_registration_view(self):
        url=reverse("register_student")
        data={"first_name":self.student.first_name,
              "last_name":self.student.last_name,
              "age":self.student.age,
              }
        request=self.client.POST(url,data)
        self.assertEqual(request.status_code,200)



# Create your tests here.
