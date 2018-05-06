from django.db import models


GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)

YEAR_CHOICES = (
   ('FE', 'First Year'),
   ('SE', 'Second Year'),
   ('TE', 'Third Year'),
   ('BE', 'Final Year'),
)

CLASS_CHOICES = (
   ('I', 'First'),
   ('II', 'Second')
)


class UserDetails(models.Model):
    sap = models.CharField(max_length=50)
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=500)
    access = models.BooleanField(default=False)
    address = models.CharField(max_length=1000)

    def __str__(self):
        return self.username


class FormDetails(models.Model):
    sap = models.CharField(max_length=50)
    dept = models.CharField(max_length=250)
    date_of_birth = models.DateField(default=None)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
    year = models.CharField(choices=YEAR_CHOICES, max_length=128)
    train_class = models.CharField(choices=CLASS_CHOICES, max_length=128)
    date = models.DateTimeField(auto_now_add=True)
    station = models.CharField(max_length=250)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.sap


class ChangeUserDetails(models.Model):
    sap = models.CharField(max_length=50)
    dept = models.CharField(max_length=250)
    year = models.CharField(choices=YEAR_CHOICES, max_length=128)
    date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=1000)
    station = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    address_proof = models.FileField()

    def __str__(self):
        return self.sap
