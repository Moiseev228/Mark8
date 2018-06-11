from __future__ import unicode_literals
from django.shortcuts import render
from administration_app.models import Staff
from extract_app.models import Recepts
from .models import Patiens
from .models import Prepations
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
import django

def get_main_page(request):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'registry':
            return render(request, 'registry_app/main.html', {})
        else:
            auth.logout(request)
            return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')


def get_preparations_page(request):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'registry':
            preparations = Prepations.objects.all()
            flag_view_additional_info = False
            return render(request, 'registry_app/preparations.html', {'preparations':preparations, 'flag_view_additional_info':flag_view_additional_info})
        else:
            auth.logout(request)
            return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')

def get_preparation(request, id_preparations=1):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'registry':
            return_objects_preparations = []
            preparations = Prepations.objects.all()
            for item in preparations:
                preparation = {}
                preparation['id'] = item.id
                preparation['name'] = item.name
                preparation['type_prepations'] = item.type_prepations
                return_objects_preparations.append(preparation)

            flag_view_additional_info = True;

            return_objects_preparation = {}
            preparation = Prepations.objects.get(id=id_preparations)
            return_objects_preparation['name'] =  preparation.name
            return_objects_preparation['type_prepations'] = preparation.type_prepations
            return_objects_preparation['maker'] = preparation.maker
            return_objects_preparation['form_release'] = preparation.form_release

            prescriptions_issued = []
            prescriptions_issued.extend(Recepts.objects.filter(id_prepations=id_preparations))
            return_objects_preparation['prescriptions_issued'] = []
            for item in prescriptions_issued:
                ssued = {}
                ssued['name'] = Prepations.objects.get(id=item.id_prepations).name
                ssued['name_patient'] = Patiens.objects.get(id=item.id_patiens).name
                ssued['date_issue'] = item.date_issue
                return_objects_preparation['prescriptions_issued'].append(ssued)               
            return render(request, 'registry_app/preparations.html', {'preparation':return_objects_preparation, 
            'preparations':return_objects_preparations,'flag_view_additional_info':flag_view_additional_info})
        else:
            auth.logout(request)
            return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')

def get_patients_page(request):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'registry':
            patiens = Patiens.objects.all()
            flag_view_additional_info = False
            return render(request, 'registry_app/patients.html', {'patiens':patiens, 'flag_view_additional_info':flag_view_additional_info})
        else:
            auth.logout(request)
            return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')

def get_patient(request, id_patients=1):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'registry':
            patiens = Patiens.objects.all()
            flag_view_additional_info = True
            return render(request, 'registry_app/patients.html', {'patiens':Patiens.objects.get(id=id_patients), 
            'patiens':patiens,'flag_view_additional_info':flag_view_additional_info})
        else:
            auth.logout(request)
            return redirect('/logsys/login')
    else:
        return redirect('/logsys/login') 


def new_patient(request):
    if request.is_ajax():
        if request.method == 'GET':
            patient = Patiens.objects.filter(polis=request.GET['polis'])
            if len(patient) != 0:
                return HttpResponse('repit_polis', content_type='text/html')
            else:
                patient = Patiens(name=request.GET['name'],
                    address=request.GET['address'],
                    polis=request.GET['polis'],
                    phone=request.GET['phone'],
                    sector=request.GET['sector'],
                    Recording_date=request.GET['Recording_date'])
                patient.save()
                return HttpResponse('ok', content_type='text/html')
    else:
        return HttpResponse('no', content_type='text/html')
    