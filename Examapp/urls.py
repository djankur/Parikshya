from django.contrib import admin
from django.urls import path
from Examapp import views

urlpatterns = [
    path('/', views.home, name='home'),
    path('regform/',views.regform,name='regform'),
    path('stdlogin/',views.stdlogin,name='stdlogin'),
    path('qn/',views.qn,name='qn'),
    path('tealogin/',views.tealogin,name='tealogin'),
    path('addqn/',views.addqn,name='addqn'),
    path('tindex/',views.tindex,name='tindex'),
    path('sindex/',views.sindex,name='sindex'),
    path('logout',views.logout,name='logout'),
    path('saves/',views.saves,name='saves'),
    path('result/',views.result,name='result'),
    path('viewqn/',views.viewqn,name='viewqn'),
    path('tresult/',views.tresult,name='tresult'),
    path('delete/',views.delete,name='delete'),
    path('edit/',views.edit,name='edit'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
   
]

#  path('', views.index, name='index'),