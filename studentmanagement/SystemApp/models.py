
from django.db import models

# Create your models here.
class City(models.Model):
    City_Name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.City_Name}"

class Course(models.Model):
    Course_Name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.Course_Name}"


class Student(models.Model):
    Stu_Name = models.CharField(max_length=50)
    Stu_Age = models.IntegerField()
    Stu_Pno = models.BigIntegerField()
    Stu_City = models.ForeignKey(City,on_delete=models.CASCADE)
    Stu_Course = models.ForeignKey(Course,on_delete=models.CASCADE)



