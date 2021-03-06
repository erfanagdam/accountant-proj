from django.db import models
from jdatetime import date as jdate
from django_jalali.db import models as jmodels
from django.contrib.auth.models import User
# Create your models here.

class exp(models.Model):
    title = models.CharField(max_length= 200)
    amount = models.BigIntegerField()
    date = jmodels.jDateField(default = jdate.today(), help_text="** ..   default is today | example : 1399-01-08   ..  **")
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return "{}::{}::{}".format(self.title, self.amount, self.date.strftime(' %d %b %Y '))

class income(models.Model):
    title = models.CharField(max_length= 200)
    amount = models.BigIntegerField()
    date = jmodels.jDateField(default = jdate.today(), help_text="** ..   default is today | example : 1399-01-08   ..  **")
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return "{}::{}::{}".format(self.title, self.amount, self.date.strftime(' %d %b %Y '))

class token(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    token = models.CharField(max_length = 48)

    def __str__(self):
        return "{}".format(self.user)
