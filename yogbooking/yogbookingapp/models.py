from django.db import models

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=50, default='')
    price = models.IntegerField(default='0')
    description = models.CharField(max_length=1000,default="")
    id = models.CharField(max_length=20,default="",primary_key = True)
    image = models.ImageField(upload_to="yogbookingapp/images")
    def __str__(self):
        return self.name
class Events(models.Model):
    name = models.CharField(max_length=20, default="")
    description = models.CharField(max_length=1000,default="")
    image = models.ImageField(upload_to="images")
    def __str__(self):
        return self.name
    #hello
class Blog(models.Model):
    name = models.CharField(max_length=20, default="")
    img1 = models.ImageField(upload_to="yogbookingapp/images")
    img2 = models.ImageField(upload_to="yogbookingapp/images")
    text = models.CharField(max_length=2000, default="")
    def __str__(self):
        return self.name
class Instructor(models.Model):
        name = models.CharField(max_length=20, default="")
        fathers_name = models.CharField(max_length=20, default="")
        aadhar = models.IntegerField(default='0')
        address = models.CharField(max_length=20, default="")
        experiance = models.CharField(max_length=20, default="")
        city = models.CharField(max_length=50, default="")
        resume = models.FileField(upload_to='yogbookingapp/pdf')
        profile = models.ImageField(upload_to="yogbookingapp/images")
        rating = models.IntegerField(default=0)
        def __str__(self):
            return self.name
class Booking(models.Model):
    city = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=20, default="")
    no_of_students = models.IntegerField(default=0)
    date_of_event = models.DateField()
    def __str__(self):
        return self.name
class User(models.Model):
    name = models.CharField(max_length=20, default="")
    fathers_name = models.CharField(max_length=20, default="")
    aadhar = models.IntegerField(default='0')
    address = models.CharField(max_length=20, default="")
    city = models.CharField(max_length=50, default="")
    profile = models.ImageField(upload_to="yogbookingapp/images")
    proffession = models.CharField(max_length=20, default="")
    gender = models.CharField(max_length=5, default=0)
    def __str__(self):
        return self.name
class Upcommingevent(models.Model):
    name =models.CharField(max_length=50,default="")
    date = models.DateField()
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="yogbookingapp/images")
    id = models.CharField(max_length=30,primary_key = True)
    def __str__(self):
        return self.name
