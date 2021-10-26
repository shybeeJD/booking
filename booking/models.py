from django.db import models

# Create your models here.

unit_choice = (
		(0, 'hour'),
		(1, 'day'),
        (2, 'month'),
	)

category_choice= (
		(0, 'walk-in'),
		(1, 'reservation'),
	)
class facility_type(models.Model):
    typeId = models.IntegerField()
    facility = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    ac_socket = models.IntegerField()
    locker = models.IntegerField()
    cabinet = models.IntegerField()
    seat= models.IntegerField()
    projector = models.IntegerField()
    def __str__(self):
        return "%s" % (self.typeId)


class office_location(models.Model):
    centerId=models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    flat = models.CharField(max_length=20)
    floor = models.IntegerField()
    building =models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    tel=models.CharField(max_length=100)
    admin = models.CharField(max_length=100)


class facility(models.Model):
    facility_id = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    centerId= models.CharField(max_length=100)
    typeId= models.CharField(max_length=100)
    price = models.CharField(max_length=100)

class plan(models.Model):
    planId = models.IntegerField(primary_key=True)
    typeId=models.IntegerField()
    unit = models.IntegerField(choices=unit_choice)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.IntegerField(choices=category_choice)


class member_plan(models.Model):
    planId= models.IntegerField()
    userId = models.IntegerField()
    buy_time = models.DateTimeField(auto_now_add=True)

class facility_reservering(models.Model):
    facility_id = models.CharField(max_length=100)
    userId = models.IntegerField()
    begin_time = models.IntegerField()
    during = models.IntegerField()
    create_time=models.DateTimeField(auto_now_add=True)




