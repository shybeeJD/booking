from django.db import models

# Create your models here.
sex_choice = (
		(0, 'Female'),
		(1, 'Male'),
	)


class Member(models.Model):
    userId = models.BigAutoField(primary_key=True)
    userName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    gender = models.IntegerField(choices=sex_choice,default=1)
    tel = models.CharField(max_length=30)
    address = models.CharField(max_length=256)
    email = models.CharField(max_length=100)
    passwd= models.CharField(max_length=256)
    admin = models.BooleanField(default=False)
    def __str__(self):
        return "%s" % (self.userId)