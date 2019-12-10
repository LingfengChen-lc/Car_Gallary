from django.db import models
from storage import MyStorage
# Create your models here.

from django.contrib.auth.models import User

from django.core.exceptions import ValidationError

# class UserProfile(models.Model):
#     user   = models.OneToOneField(User)
#     avatar = models.ImageField()

def validate_rate_range(value):
    if value < 0 or value > 100:
        raise ValidationError('range of score between 0-100')

class Company(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)

class Car(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    miles = models.IntegerField()
    out_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='media/', storage=MyStorage())
    rate = models.IntegerField(null=True, validators=[validate_rate_range])
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)



