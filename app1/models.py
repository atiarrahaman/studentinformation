from django.db import models

# Create your models here.


class Student_class(models.Model):
    name= models.CharField( max_length=50)

    def __str__(self):
        return self.name

class Division (models.Model):

    division= models.CharField( max_length=50)
    def __str__(self):
        return self.division

class Distic (models.Model):
    distic= models.CharField( max_length=50)
    division=models.ForeignKey('Division', on_delete=models.CASCADE)
    def __str__(self):
        return self.distic

class Students_info(models.Model):

    name= models.CharField(max_length=50)
    roll= models.IntegerField()
    address= models.CharField(max_length=50)
    phone= models.CharField( max_length=50)
    student_class= models.ForeignKey('Student_class', on_delete=models.CASCADE)
    distic= models.ForeignKey('Distic', on_delete=models.CASCADE)
    def __str__(self):
        return self.name















    