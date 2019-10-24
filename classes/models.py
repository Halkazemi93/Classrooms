from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# from model_utils import Choices

class Classroom(models.Model):
	teacher = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	year = models.IntegerField()

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})


class Student(models.Model):
	GENDER_CHOICES = (('MALE', "Male"), ('FEMALE', 'Female'))
	name = models.CharField(max_length=105)
	date_of_birth = models.DateField()
	gender =models.CharField(max_length=9, choices=GENDER_CHOICES)
	exam_grade = models.CharField(max_length=2)
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
