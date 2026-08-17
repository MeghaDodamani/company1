from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length= 200)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8 ,decimal_places=2)
    dep_no = models.ForeignKey('Department',on_delete=models.CASCADE,related_name='employees')

    def __str__(self):
      return self.name

class Department(models.Model):
    dep_id = models.IntegerField(primary_key=True)
    dep_name = models.CharField(max_length=200)
    def __str__(self):
      return self.dep_name

