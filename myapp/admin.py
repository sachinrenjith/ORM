from django.contrib import admin
from myapp.models import Teacher,Course,Chapter,Lesson
# Register your models here.
 
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Chapter)