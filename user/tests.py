from django.test import TestCase

# Create your tests here.

from user.models import Member
mem=Member(userId=1001,userName='Admin_KT01',
           firstName='Staff01',lastName='Staff01',gender=1,tel='64244821',
           address='Kwun Tong',email='admin_kt01@gamil.com',admin=False,passwd='123')
mem.save()