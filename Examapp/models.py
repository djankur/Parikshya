from django.db import models

# Create your models here.
class Registration(models.Model):
    StudentID =models.AutoField
    name = models.CharField(max_length=255,null='false')
    address = models.CharField(max_length=255,null='false')
    pin = models.CharField(max_length=122,null='false')
    email = models.EmailField(max_length=122,null='false')
    phone = models.CharField(max_length=12,null='false')
    password = models.CharField(max_length=255,null='false')
    date= models.DateField()

class Teacher(models.Model):
    Tid=models.AutoField
    username=models.CharField(max_length=50,null='false')
    password=models.CharField(max_length=30,null='false')
    date=models.DateField()

class Question(models.Model):
    qid=models.CharField(max_length= 255,null='false')
    question=models.CharField(max_length= 255,null='false')
    option1=models.CharField(max_length=255,null='false')
    option2=models.CharField(max_length=255,null='false')
    option3=models.CharField(max_length=255,null='false')
    option4=models.CharField(max_length=255,null='false')
    correctans=models.CharField(max_length=255,null='false')
class Result(models.Model):
    exam_name=models.CharField(max_length= 255,null='false')
    marks=models.IntegerField()
    s_email=models.CharField(max_length=255,null='false')
    sname=models.CharField(max_length=255,null='false')

    