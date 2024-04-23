from django.db import models

# Create your models here.

class Person(models.Model):
    firstname = models.CharField("Person's first name", max_length=50)
    lastname = models.CharField("LastName",max_length =30)
    created_date = models.DateTimeField(auto_now=True)
    age = models.IntegerField(default = 0)
    profile_pics = models.ImageField("Profile Pics" ,upload_to='profile_pics', blank = True, null = True)

    def __str__ (self):
      return self.firstname + " " + self.lastname 
    

#class Profile(models.Model):
   #person = models.OneToOneField(Person, on_delete = models.CASCADE)
   #nickname = models.CharField(max_length = 50)
   #bio = models.CharField(max_length=80)

   #def __str__(self):
      #return self.person.firstname + " " + self.nickname
