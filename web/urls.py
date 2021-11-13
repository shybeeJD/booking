"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from  user.views import *
import booking.views as book
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ping/', ping),
    path('user/login/', login),
    path('user/register/', register),
    path('user/change_passwd/', change_passwd),
    path('user/logout/', logout),
    path('manage/get_admin/', book.get_admin),
    path('manage/add_facility_type/', book.add_facility_type),
    path('manage/add_office_location/', book.add_office_location),
    path('manage/get_office/', book.get_office),
    path('manage/get_facility_type/', book.get_facility_type),
    path('manage/add_facility/', book.add_facility),
    path('manage/get_facility/', book.get_facility),
    path('manage/get_reserve_price/', book.get_reserve_price),
    path('manage/get_day_ava/', book.get_day_ava),
    path('manage/get_hour_ava/', book.get_hour_ava),
    path('manage/add_plan/', book.add_plan),
    path('manage/get_plan/', book.get_plan),
    path('manage/buy_plan/', book.buy_plan),
    path('manage/get_member_plan/', book.get_member_plan),
    path('manage/add_reserve/', book.add_reserve),
    path('manage/update_user_info/', update_user_info),
    path('manage/cancel_reserve/', book.cancel_reserve),
    path('manage/get_all_users/', book.get_all_users),
    path('manage/get_all_user_reserve/', book.get_all_user_reserve),
]
