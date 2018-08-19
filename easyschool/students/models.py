from django.db import models

# Create your models here.
class Student(models.Model):
    admission_no    = models.IntegerField(unique=True)
    first_name      = models.CharField(max_length=30)
    last_name       = models.CharField(max_length=30)
    date_of_birth   = models.DateField()
    father_name     = models.CharField(max_length=50)
    father_cnic     = models.CharField(max_length=13)
    fathers_phone_no= models.CharField(max_length=11, default="0000000")
    fathers_proffesion= models.CharField(max_length=50, default="Not Set")
    address         = models.CharField(max_length=150, default="Not Set")


    def __str__(self):
        return self.first_name+' '+self.last_name
    
    def __repr__(self):
        return 'Student(Adm:'+self.admission_no+', name:'+self.__str__()
