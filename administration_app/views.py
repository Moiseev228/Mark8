# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Staff
from extract_app.models import Recepts
from registry_app.models import Patiens
from registry_app.models import Prepations
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
import django
from django.http import JsonResponse
from django.shortcuts import render_to_response
import json
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.
def get_main_page(request):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'administration':
            return render(request, 'administration_app/main.html', {})
        else:
            auth.logout(request)
            return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')


def get_staff_page(request):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'administration':
            return_objects = []
            staff = Staff.objects.all()
            for item in staff:
                employee = {}
                employee['id'] = item.id
                name_employee = User.objects.get(username=item.login_employee).first_name + ' ' + User.objects.get(username=item.login_employee).last_name
                employee['name'] = name_employee
                employee['post'] = item.post
                employee['specialization'] = item.specialization
                return_objects.append(employee)
            flag_view_additional_info = False
            return_objects.reverse()
            return render(request, 'administration_app/staff.html', {'staff':return_objects, 'flag_view_additional_info':flag_view_additional_info})
        else:
            auth.logout(request)
            return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')

def get_employee(request, id_employees=1):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'administration':
            return_objects_staff = []
            staff = Staff.objects.all()
            for item in staff:
                employee = {}
                employee['id'] = item.id
                name_employee = User.objects.get(username=item.login_employee).first_name + ' ' + User.objects.get(username=item.login_employee).last_name
                employee['name'] = name_employee
                employee['post'] = item.post
                employee['specialization'] = item.specialization
                return_objects_staff.append(employee)

            flag_view_additional_info = True

            return_objects_employee = {}
            employee = Staff.objects.get(id=id_employees)
            name_employee = User.objects.get(username=employee.login_employee).first_name + ' ' + User.objects.get(username=employee.login_employee).last_name
            return_objects_employee['name'] = name_employee
            return_objects_employee['post'] = employee.post
            return_objects_employee['specialization'] = employee.specialization
            return_objects_employee['phone'] = employee.phone
            return_objects_employee['address'] = employee.address
            return_objects_employee['passport'] = employee.passport

            prescriptions_issued = []
            prescriptions_issued.extend(Recepts.objects.filter(id_staff=id_employees))
            return_objects_employee['prescriptions_issued'] = []
            for item in prescriptions_issued:
                ssued = {}
                ssued['name'] = Prepations.objects.get(id=item.id_prepations).name
                ssued['name_patient'] = Patiens.objects.get(id=item.id_patiens).name
                ssued['date_issue'] = item.date_issue
                return_objects_employee['prescriptions_issued'].append(ssued)
            return render(request, 'administration_app/staff.html', {'employee':return_objects_employee, 
            'staff':return_objects_staff,'flag_view_additional_info':flag_view_additional_info})
        else:
            auth.logout(request)
            return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')

def get_preparations_page(request):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'administration':
            preparations = Prepations.objects.all()
            flag_view_additional_info = False
            return render(request, 'administration_app/preparations.html', {'preparations':preparations, 'flag_view_additional_info':flag_view_additional_info})
        else:
            auth.logout(request)
            return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')

def get_preparation(request, id_preparations=1):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'administration':
            preparations = Prepations.objects.all()
            flag_view_additional_info = True
            return render(request, 'administration_app/preparations.html', {'prepation':Prepations.objects.get(id=id_preparations), 
            'preparations':preparations,'flag_view_additional_info':flag_view_additional_info})
        else:
            auth.logout(request)
            return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')

def get_recepts_page(request):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'administration':
            recepts = []
            recepts_info = Recepts.objects.all()
            for recept_info in recepts_info:
                recept = {}
                recept['name_patients'] = Patiens.objects.get(id=recept_info.id_patiens).name
                login = Staff.objects.get(id=recept_info.id_staff).login_employee
                recept['name_employee'] = User.objects.get(username=login).first_name + ' ' + User.objects.get(username=login).last_name
                recept['date_issue'] =  recept_info.date_issue
                recepts.append(recept)
                print(recept)
            flag_view_additional_info = False;
            return render(request, 'administration_app/recepts.html', {'recepts':recepts, 'flag_view_additional_info':flag_view_additional_info})
        else:
            auth.logout(request)
            return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')

def get_recept(request, id_recepts=1):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'administration':
            recepts = []
            recepts_info = Recepts.objects.all()
            for recept_info in recepts_info:
                recept = {}
                recept['name_patients'] = Patiens.objects.get(id=recept_info.id_patiens).name
                login = Staff.objects.get(id=recept_info.id_staff).login_employee
                recept['name_employee'] =  User.objects.get(username=login).first_name + ' ' + User.objects.get(username=login).last_name
                recept['date_issue'] =  recept_info.date_issue
                recepts.append(recept)
            seleted_recept = Recepts.objects.get(id=id_recepts)
            seleted_recept_for_templade = {}
            seleted_recept_for_templade['name_patients'] = Patiens.objects.get(id=seleted_recept.id_patiens).name
            login = Staff.objects.get(id=seleted_recept.id_staff).login_employee
            seleted_recept_for_templade['name_employee'] = User.objects.get(username=login).first_name + ' ' + User.objects.get(username=login).last_name
            
            seleted_recept_for_templade['date_issue'] =  seleted_recept.date_issue
            flag_view_additional_info = True;
            return render(request, 'administration_app/recepts.html', {'recept':seleted_recept_for_templade, 
            'recepts':recepts,'flag_view_additional_info':flag_view_additional_info})
        else:
            auth.logout(request)
            return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')

def get_patients_page(request):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'administration':
            patiens = Patiens.objects.all()
            flag_view_additional_info = False
            return render(request, 'administration_app/patients.html', {'patiens':patiens, 'flag_view_additional_info':flag_view_additional_info})
        else:
            auth.logout(request)
            return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')

def get_patient(request, id_patients=1):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'administration':
            patiens = Patiens.objects.all()
            flag_view_additional_info = True
            return render(request, 'administration_app/patients.html', {'patien':Patiens.objects.get(id=id_patients), 
            'patiens':patiens,'flag_view_additional_info':flag_view_additional_info})
        else:
            auth.logout(request)
            return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')


def new_employee(request):
    if request.is_ajax():
        if request.method == 'GET':
            try:
                user = User.objects.create_user(username=request.GET['login'], password=request.GET['password'], first_name=request.GET['name'], last_name=request.GET['lastname'])
            except django.db.utils.IntegrityError as ex:
                return HttpResponse('repit_login', content_type='text/html')
            else:
                employee = Staff(login_employee=request.GET['login'],
                    type_users=request.GET['type_users'],
                    address=request.GET['address'],
                    phone=request.GET['phone'],
                    post=request.GET['post'],
                    specialization=request.GET['specialization'],
                    passport=request.GET['passport'])
                employee.save()
            return HttpResponse('ok', content_type='text/html')
    else:
        return HttpResponse('no', content_type='text/html')




###################### ПОИСК #######################

def staff_search(request):
    if request.method == 'GET':
        flag_view_additional_info = False
        search_term = request.GET['search_term']
        staff = []
        return_object = []
        staff.extend(User.objects.filter(first_name=search_term))
        staff.extend(User.objects.filter(last_name=search_term))
        for item in staff:
            employee = {}
            employee['id'] = Staff.objects.get(login_employee=item.username).id
            employee['name'] = item.first_name + ' ' + item.last_name
            employee['post'] = Staff.objects.get(login_employee=item.username).post
            employee['specialization'] = Staff.objects.get(login_employee=item.username).specialization
            return_object.append(employee)
        staff = []
        staff.extend(Staff.objects.filter(specialization=search_term))
        staff.extend(Staff.objects.filter(post=search_term))
        for item in staff:
                employee = {}
                employee['id'] = item.id
                name_employee = User.objects.get(username=item.login_employee).first_name + ' ' + User.objects.get(username=item.login_employee).last_name
                employee['name'] = name_employee
                employee['post'] = item.post
                employee['specialization'] = item.specialization
                return_object.append(employee)

        return render(request, 'administration_app/staff.html', 
            {'staff':return_object, 'flag_view_additional_info':flag_view_additional_info})
    else:
        return render(request, 'administration_app/staff.html', 
            {'flag_view_additional_info':flag_view_additional_info})
            
   
        
        