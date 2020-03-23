from django.db import models
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

class exp(models.Model):
    title = models.CharField(max_length= 200)
    amount = models.BigIntegerField()
    date = models.DateField(default=date.today )
    #user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return "{}---:{}".format(self.title, self.date.strftime(' %b %e %y '))

class income(models.Model):
    title = models.CharField(max_length= 200)
    amount = models.BigIntegerField()
    date = models.DateField(default=date.today )
    #user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return "{}---:{}".format(self.title, self.date.strftime(' %b %e %y '))

class token(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    token = models.CharField(max_length = 48)

    def __str__(self):
        return "{}".format(self.user)
