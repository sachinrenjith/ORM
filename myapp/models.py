from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class User(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     username = models.CharField(max_length=20, unique= False)
#     email = models.EmailField(max_length=30, unique=False)

#     def __str__(self):
#         return self.first_name
    
class Teacher(models.Model):
    teacher_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.teacher_name

class Course(models.Model):
    course_name = models.CharField(max_length=30)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return self.course_name

class Lesson(models.Model):
    lesson_name = models.CharField(max_length=30)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.lesson_name

class Chapter(models.Model):
    chapter_name = models.CharField(max_length=30)
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    index_number = models.IntegerField() 

    def __str__(self):
        return self.chapter_name       


