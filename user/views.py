from django.shortcuts import render

# Create your views here.
from user.models import Member
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random
import hashlib
from django.conf import settings
def ping(request):

    return JsonResponse({'res':'pong'})



def login(request):
    email =request.POST.get('email')
    passwd = request.POST.get('passwd')
    res = Member.objects.filter(email=email,passwd=passwd)

    if len(res)>0:
        h=hashlib.md5()
        rand=random.random()
        h.update(str(rand).encode(encoding='utf-8'))


        jessionId =h.hexdigest()

        request.session['userId']=res[0].userId
        request.session['jessionId']=jessionId
        resp=JsonResponse({'status':'success'})
        return resp
    return JsonResponse({'status': 'failed'})

def register(request):

    passwd = request.POST.get('passwd')
    userName = request.POST.get('userName')
    firstName = request.POST.get('firstName')
    lastName = request.POST.get('lastName')
    gender = request.POST.get('gender')
    tel = request.POST.get('tel')
    address = request.POST.get('address')
    email = request.POST.get('email')
    try:
        new_user=Member(

            passwd=passwd,
            userName=userName,
            firstName=firstName,
            lastName=lastName,
            gender=gender,
            tel=tel,
            address=address,
            email=email,
        )
        new_user.save()
        return JsonResponse({'status': 'success'})
    except Exception as e:
        print(e)
        return JsonResponse({'status': 'failed'})


def change_passwd(request):
    email = request.POST.get('email')
    passwd = request.POST.get('passwd')
    new_passwd=request.POST.get('new_passwd')
    res = Member.objects.filter(email=email, passwd=passwd)
    if len(res)>0:
        res[0].passwd=new_passwd
        res[0].save()
        resp=JsonResponse({'status':'success'})
        return resp
    return JsonResponse({'status': 'failed'})

def logout(request):
    try:
        del request.session['jessionId']
    except:
        pass
    return JsonResponse({'status':'success'})