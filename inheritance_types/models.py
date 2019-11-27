from django.db import models

# Create your models here.
class basemodel(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    username=models.CharField(max_length=20)

    class Meta:
        abstract=True


class student(basemodel):
   address=models.CharField(max_length=20)
   marks=models.IntegerField()

   def __str__(self):
       return self.username

   def fullname(self):
       return self.first_name + "" + self.last_name


class employee(basemodel):
    pass

    def __str__(self):
        return self.username
class product(models.Model):
    pname=models.CharField(max_length=10)
    pmfdt=models.DateField()
    pexpdt=models.DateField()

    def __str__(self):
        return self.pname

class proxy(product):
    class Meta:
        ordering=('pname',)
        proxy=True
    def fun(self):
        return self.pname
