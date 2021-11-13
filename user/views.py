from django.shortcuts import render

# Create your views here.
from user.models import Member,sex_choice
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random
import hashlib
from user.models import sex_choice
from django.conf import settings
from django.forms.models import model_to_dict
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
        request.session['admin'] = res[0].admin
        resp=JsonResponse({'status':'success','user':model_to_dict(res[0])})
        return resp
    resp = JsonResponse({'status': 'failed'})
    return resp


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

def get_user_info(request):
    userId = request.session.get('userId')
    try:
        user = Member.objects.get(userId=userId)
        return JsonResponse({'status':'success','user':model_to_dict(user)})
    except:
        return JsonResponse({'status': 'failed'})

def update_user_info(request):

    userName = request.POST.get('userName')
    firstName = request.POST.get('firstName')
    lastName = request.POST.get('lastName')
    gender = request.POST.get('gender')
    tel = request.POST.get('tel')
    address =request.POST.get('address')
    userId = request.session.get('userId')
    try:
        user = Member.objects.filter(userId=userId).update(
            userName = userName,
            firstName=firstName,
            lastName=lastName,
            gender=dict((key,value) for (value,key) in sex_choice)[gender],
            tel=tel,
            address=address,
        )


        return JsonResponse({'status':'success'})
    except Exception as e:
        print(e)

        return JsonResponse({'status': 'failed'})

def get_user_by_Id(request):
    isadmin = request.session.get('admin')
    userId = request.GET.get('userId')

    user_now = request.session.get('userId')
    if not isadmin and str(user_now) != str(userId):
        return JsonResponse({'status': 'failed, no access'})
    try:
        user = Member.objects.get(userId=userId)
        return JsonResponse({'status': 'success', 'user': model_to_dict(user)})
    except:
        return JsonResponse({'status': 'failed'})