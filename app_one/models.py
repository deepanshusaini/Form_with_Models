from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    roll_no = models.PositiveSmallIntegerField(primary_key=True)
    
    def __str__(self):
        return self.name