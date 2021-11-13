from django.shortcuts import render

# Create your views here.
from booking.models import *
from user.models import Member
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
import datetime
from user.models import Member
import json
def last_day_of_month(any_day):
    """
    获取获得一个月中的最后一天
    :param any_day: 任意日期
    :return: string
    """
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)
def add_facility_type(request):
    try:
        facility = request.POST.get('facility')
        description = request.POST.get('description')
        ac_socket = request.POST.get('ac_socket')
        locker = request.POST.get('locker')
        cabinet = request.POST.get('cabinet')
        seat = request.POST.get('seat')
        projector = request.POST.get('projector')
        hour_price=request.POST.get('hour_price')
        day_price = request.POST.get('day_price')
        week_price = request.POST.get('week_price')
        month_price=request.POST.get('month_price')
        new_facility_type = facility_type(
            facility=facility,
            description=description,
            ac_socket=ac_socket,
            locker=locker,
            cabinet=cabinet,
            seat=seat,
            projector=projector,
            hour_price=hour_price,
            day_price=day_price,
            week_price=week_price,
            month_price=month_price
        )
        new_facility_type.save()
        return JsonResponse({'status':'success'})
    except Exception as e:
        print(e)
        return JsonResponse({'status': 'failed'})
        pass

def add_office_location(request):
    try:
        centerId = request.POST.get('centerId')
        district = request.POST.get('district')
        flat = request.POST.get('flat')
        floor = request.POST.get('floor')
        building = request.POST.get('building')
        street = request.POST.get('street')
        tel = request.POST.get('tel')
        admin = request.POST.get('admin')
        new_office_location=office_location(
            centerId=centerId,
            district=district,
            flat=flat,
            floor=floor,
            building=building,
            street=street,
            tel=tel,
            admin=admin
        )
        new_office_location.save()
        return JsonResponse({'status': 'success'})
        pass

    except:
        return JsonResponse({'status': 'failed'})
        pass

def get_admin(request):
    res= Member.objects.filter(admin=True)
    admin=[]
    for ad in res:
        admin.append(ad.userName)
    return JsonResponse({'admin':admin})

def get_office(request):
    isadmin = request.session.get('admin')
    print(isadmin)
    res = office_location.objects.all()
    data = []
    for i in res:
        data.append(model_to_dict(i))
    return JsonResponse({'data': data})

def get_facility_type(request):

    res = facility_type.objects.all()
    data = []
    for i in res:
        data.append(model_to_dict(i))
    return JsonResponse({'data': data})

def get_facility(request):
    center_ID=request.GET.get('center_ID')
    if center_ID:

        res = facility.objects.filter(
            centerId=center_ID
        )
    else:
        res =facility.objects.all()
    data = []
    for i in res:
        data.append(model_to_dict(i))
    return JsonResponse({'data': data})

def add_facility(request):
    try:
        isadmin = request.session.get('admin')
        if not isadmin:
            return JsonResponse({'status': 'failed'})
            pass
        facility_id = request.POST.get('facility_id')
        number = request.POST.get('number')
        centerId = request.POST.get('centerId')
        typeId = request.POST.get('typeId')

        new_facility=facility(
            facility_id=facility_id,
            number=number,
            centerId=centerId,
            typeId=typeId,
        )
        new_facility.save()
        return JsonResponse({'status': 'success'})
        pass

    except:
        return JsonResponse({'status': 'failed'})
        pass
    pass

def add_plan(request):
    try:
        isadmin = request.session.get('admin')
        if not isadmin:
            return JsonResponse({'status': 'failed'})
        typeId = request.POST.get('typeId')
        unit = request.POST.get('unit')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category = request.POST.get('category')

        new_plan=plan(
            typeId=typeId,
            unit=unit,
            description=description,
            price=price,
            category=category
        )
        new_plan.save()
        return JsonResponse({'status': 'success'})
        pass

    except Exception as e:
        print(e)
        return JsonResponse({'status': 'failed'})
        pass
    pass
def get_plan(request):
    res = plan.objects.all()
    data = []
    for i in res:
        data.append(model_to_dict(i))
    return JsonResponse({'data': data})

def buy_plan(request):
    operater_id  = request.session.get('userId')

    planId = request.POST.get('planId')
    userId = request.POST.get('userId')
    num = request.POST.get('num')
    print(num)
    isadmin = request.session.get('admin')
    user_now = request.session.get('userId')
    if not isadmin and user_now != userId:
        return JsonResponse({'status': 'failed, no access'})
    try:
        operater = Member.objects.get(userId=operater_id,admin=True)
    except:
        return JsonResponse({'status': 'failed, no such operater'})
    if operater.admin:
        for i in range(int(num)):
            new_member_plan = member_plan(
                planId=planId,
                userId=userId
            )
            new_member_plan.save()
            return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'failed','message':'no auth'})

def get_member_plan(request):
    userId  = request.session.get('userId')
    isadmin = request.session.get('admin')
    user_now = request.session.get('userId')
    if not isadmin and user_now != userId:
        return JsonResponse({'status': 'failed, no access'})
    res = member_plan.objects.filter(userId=userId)
    data = []
    for i in res:
        data.append(model_to_dict(i))
    return JsonResponse({'data': data})

def add_reserve(request):
    facility_id = request.POST.get('facility_id')
    typeId= request.POST.get('typeId')
    userId = request.POST.get('userId')
    unit = request.POST.get('unit')
    year = request.POST.get('year')
    month = request.POST.get('month')
    days = request.POST.get('days')
    hours =request.POST.get('hours')
    days=json.loads(days)
    hours=json.loads(hours)
    operater_id = request.POST.get('operater_id')
    print(hours,days)
    isadmin = request.session.get('admin')
    user_now = request.session.get('userId')
    if not isadmin and user_now != userId:
        return JsonResponse({'status': 'failed, no access'})
    try:
        operater= Member.objects.get(userId=operater_id)
        if operater.admin:
            if unit == '0':
                res_hour=[]
                for hour in hours:
                    print(hour)
                    exist = facility_reservering.objects.filter(
                        facility_id=facility_id,
                        unit=unit,
                        year=year,
                        month=month,
                        day=days[0],
                        hour=hour,
                        used =True
                    )
                    if len(exist)>0:
                        print('con1')
                        continue
                    exist = facility_reservering.objects.filter(
                        facility_id=facility_id,
                        year=year,
                        month=month,
                        unit=1,
                        day=days[0],
                        used =True
                    )
                    if len(exist)>0:
                        print('con2')
                        continue
                    exist = facility_reservering.objects.filter(
                        facility_id=facility_id,
                        year=year,
                        month=month,
                        unit=2,
                        day=days[0],
                        used=True,
                    )
                    if len(exist) > 0:
                        print('con2')
                        continue
                    exist = facility_reservering.objects.filter(
                        facility_id=facility_id,
                        year=year,
                        month=month,
                        unit=3,
                        day=days[0],
                        used=True
                    )
                    if len(exist) > 0:
                        print('con2')
                        continue
                    new_reserve = facility_reservering(
                        facility_id=facility_id,
                        userId=userId,
                        unit=unit,
                        year=year,
                        month=month,
                        day=days[0],
                        hour=hour,
                        used=True
                    )
                    new_reserve.save()
                    res_hour.append(hour)
                    pass
                return JsonResponse({'status': 'success', 'hours': res_hour})
            else:
                res_day = []
                for day in days:
                    exist = facility_reservering.objects.filter(
                        facility_id=facility_id,
                        year=year,
                        month=month,
                        day=day,
                        used=True,
                    )
                    if len(exist) > 0:
                        continue
                    new_reserve = facility_reservering(
                        facility_id=facility_id,
                        userId=userId,
                        unit=unit,
                        year=year,
                        month=month,
                        day=day,
                        hour=0
                    )
                    res_day.append(day)
                    new_reserve.save()
                return JsonResponse({'status': 'success', 'days': res_day})
    except:
        print(unit=='0',1,days)

        if unit == '0':
            plan_type=plan.objects.get(unit=unit,typeId=typeId)
            member_buy=member_plan.objects.filter(userId=userId,planId=plan_type.planId,used=False)
            if len(member_buy)>=len(hours):
                for i,hour in enumerate(hours):
                    exist = facility_reservering.objects.filter(
                        facility_id=facility_id,
                        unit=unit,
                        year=year,
                        month=month,
                        day=days[0],
                        hour=hour,
                        used =True
                    )
                    if len(exist) > 0:
                        print('con1')
                        continue
                    exist = facility_reservering.objects.filter(
                        facility_id=facility_id,
                        year=year,
                        month=month,
                        unit=1,
                        day=days[0],
                        used=True,
                    )
                    if len(exist) > 0:
                        print('con2')
                        continue
                    exist = facility_reservering.objects.filter(
                        facility_id=facility_id,
                        year=year,
                        month=month,
                        unit=2,
                        day=days[0],
                        used=True
                    )
                    if len(exist) > 0:
                        print('con2')
                        continue
                    exist = facility_reservering.objects.filter(
                        facility_id=facility_id,
                        year=year,
                        month=month,
                        unit=3,
                        day=days[0],
                        used=True
                    )
                    if len(exist) > 0:
                        print('con2')
                        continue
                    new_reserve = facility_reservering(
                        facility_id=facility_id,
                        userId=userId,
                        unit=unit,
                        year=year,
                        month=month,
                        day=days[0],
                        hour=hour
                    )
                    new_reserve.save()
                    member_buy[i].used=True
                    member_buy[i].save()
                    pass
                return JsonResponse({'status': 'success', 'hours': hours})
            else:
                return JsonResponse({'status':'failed','message':'hours plan not enough'})
        elif unit=='1':
            plan_type = plan.objects.get(unit=unit,typeId=typeId)
            member_buy = member_plan.objects.filter(userId=userId, planId=plan_type.planId,used=False)
            if len(member_buy) >= len(hours):
                for i,day in enumerate(days):
                    exist = facility_reservering.objects.filter(
                        facility_id=facility_id,
                        year=year,
                        month=month,
                        day=day,
                        used=True,
                    )
                    if len(exist) > 0:
                        continue
                    new_reserve = facility_reservering(
                        facility_id=facility_id,
                        userId=userId,
                        unit=unit,
                        year=year,
                        month=month,
                        day=day,
                        hour=0,
                    )
                    new_reserve.save()
                    member_buy[i].used = True
                    member_buy[i].save()
                    pass
                return JsonResponse({'status': 'success', 'days': days})
            else:
                return JsonResponse({'status': 'failed', 'message': 'days plan not enough'})
            pass
        else:
            plan_type = plan.objects.get(unit=unit,typeId=6)
            member_buy = member_plan.objects.filter(userId=userId, planId=plan_type.planId,used=False)
            if len(member_buy) >= 1:
                for i,day in enumerate(days):
                    exist = facility_reservering.objects.filter(
                        facility_id=facility_id,
                        year=year,
                        month=month,
                        day=day,
                        used=True
                    )
                    if len(exist) > 0:
                        continue
                    new_reserve = facility_reservering(
                        facility_id=facility_id,
                        userId=userId,
                        unit=unit,
                        year=year,
                        month=month,
                        day=day,
                        hour=0
                    )
                    new_reserve.save()
                member_buy[0].used = True
                member_buy[0].save()
                pass
                return JsonResponse({'status': 'success', 'days': days})
            else:
                return JsonResponse({'status': 'failed', 'message': 'days plan not enough'})
            pass


        pass


def get_hour_ava(request):
    year = request.GET.get('year')
    month = request.GET.get('month')
    day= request.GET.get('day')
    now = datetime.datetime.now()
    if not month:
        month = now.month
    else:
        month=int(month)
    if not year:
        year = now.year
    else:
        year=int(year)
    if not day:
        day=now.day
    else:
        day=int(day)
    facility_id = request.GET.get('facility_id')
    results = facility_reservering.objects.filter(
        year=year,
        month=month,
        day=day,
        facility_id=facility_id,
        used=True
    )

    hours=[i for i in range(0,24)]


    if year==now.year and month==now.month and day==now.day:
        print(now.hour,111111)
        for i in range(0,now.hour):
            try:
                hours.remove(i)
            except:
                pass
    for result in results:
        try:
            if result.unit!=0:
                hours=[]
                break
            hours.remove(result.hour)
        except:
            pass

    return JsonResponse({'status':'success',
                         'facility_id':facility_id,
                         'hours':hours})

def get_day_ava(request):
    year = request.GET.get('year')
    month = request.GET.get('month')
    facility_id = request.GET.get('facility_id')
    print(facility_id)
    now=datetime.datetime.now()
    if not month:
        month=now.month
    else:
        month=int(month)
    if not year:
        year=now.year
    else:
        year=int(year)
    results = facility_reservering.objects.filter(
        year=year,
        month=month,
        facility_id=facility_id,
        used= True
    )
    last_day=last_day_of_month(datetime.date(year,month,1)).day
    days = [i for i in range(1,int(last_day)+1)]
    for result in results:
        try:
            days.remove(result.day)
        except:
            pass
    if year==now.year and month==now.month:
        for i in range(1,now.day):
            try:
                days.remove(i)
            except:
                pass
    if year<now.year or month<now.month:
        days=[]
    return JsonResponse({'status': 'success',
                         'facility_id': facility_id,
                         'days': days})

def get_reserve_price(request):
    facility_id = request.POST.get('facility_id')
    typeId = request.POST.get('typeId')
    try:
        res = facility_type.objects.get(typeId=typeId)
    except Exception as e:
        print(e)
        return JsonResponse({'status':'failed'})


    resp={
        'status':'success',
        'hour':res.hour_price,
        'day':res.day_price,
        'week':res.week_price,
        'month':res.month_price
    }
    return JsonResponse(resp)

def get_user_reserve(request):
    userId = request.GET.get('userId')
    isadmin = request.session.get('admin')
    user_now = request.session.get('userId')
    if not isadmin and user_now != userId:
        return JsonResponse({'status': 'failed, no access'})
    res = facility_reservering.objects.filter(userId=userId)
    data = []
    for i in res:
        data.append(model_to_dict(i))
    return JsonResponse({'data': data})
    pass

def cancel_reserve(request):
    userId = request.GET.get('userId')
    facility_id = request.GET.get('facility_id')
    isadmin = request.session.get('admin')
    id = request.session.get('id')

    user_now = request.session.get('userId')
    if not isadmin and user_now!=userId:
        return JsonResponse({'status': 'failed, no access'})


    try:
        exist = facility_reservering.objects.get(userId=int(userId),facility_id=facility_id,id=id)
        if exist.unit==0 or exist.unit==1:
            exist.used=False
            exist.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'failed'})
        pass
    except Exception as e:
        print(e)
        return JsonResponse({'status': 'failed'})
        pass
    pass

def get_all_users(request):

    isadmin = request.session.get('admin')

    if not isadmin :
        return JsonResponse({'status': 'failed, no access'})
    res = Member.objects.all()
    data = []
    for i in res:
        data.append(model_to_dict(i))
    return JsonResponse({'data': data})
    pass
def get_all_user_reserve(request):
    isadmin = request.session.get('admin')

    if not isadmin:
        return JsonResponse({'status': 'failed, no access'})
    res = facility_reservering.objects.all()
    data = []
    for i in res:
        data.append(model_to_dict(i))
    return JsonResponse({'data': data})
