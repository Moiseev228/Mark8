# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import auth
from django.shortcuts import redirect
from administration_app.models import Staff
from .models import Recepts
from registry_app.models import Patiens
from registry_app.models import Prepations
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def get_main_page(request):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'medico':
            return render(request, 'extract_app/main.html', {})
        else:
            auth.logout(request)
            return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')

def get_recepts_page(request):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'medico':
            recepts = []
            recepts_info = Recepts.objects.all()
            for recept_info in recepts_info:
                recept = {}
                recept['id'] = Recepts.objects.get(id=recept_info.id).id
                recept['name_prepations'] = Prepations.objects.get(name=recept_info.name_prepations).name                
                recept['name_patient'] = Patiens.objects.get(name=recept_info.name_patient).name
                recept['lastname_patient'] = Patiens.objects.get(lastname=recept_info.lastname_patient).lastname
                recept['patronymic_patient'] = Patiens.objects.get(patronymic=recept_info.patronymic_patient).patronymic                       
                login = Staff.objects.get(id=recept_info.id_staff).login_employee
                recept['name_employee'] = User.objects.get(username=login).first_name + ' ' + User.objects.get(username=login).last_name
                recept['date_issue'] =  recept_info.date_issue
                recepts.append(recept)
                print(recept)
            flag_view_additional_info = False;
            return render(request, 'extract_app/recepts.html', {'recepts':recepts, 'flag_view_additional_info':flag_view_additional_info})
        else:
            auth.logout(request)
            return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')


    # # if request.user.is_authenticated:
    # #     type_user = Staff.objects.get(login_employee=request.session['login']).type_users
    # #     if type_user == 'medico':
    # #         recepts = []
    # #         recepts_info = Recepts.objects.all()
    # #         for recept_info in recepts_info:
    # #             recept = {}
    # #             recept['name_patients'] = Patiens.objects.get(id=recept_info.id_patiens).name
    # #             login = Staff.objects.get(id=recept_info.id_staff).login_employee
    # #             recept['name_employee'] = User.objects.get(username=login).first_name + ' ' + User.objects.get(username=login).last_name
    # #             recept['date_issue'] =  recept_info.date_issue
    # #             recepts.append(recept)
    # #             print(recept)
    # #         flag_view_additional_info = False;
    # #         return render(request, 'extract_app/recepts.html', {'recepts':recepts, 'flag_view_additional_info':flag_view_additional_info})
    # #     else:
    # #         auth.logout(request)
    # #         return redirect('/logsys/login')
    # # else:
    # #     return redirect('/logsys/login')



def get_recept(request, id_recepts=1):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'medico':
            recepts = []
            recepts_info = Recepts.objects.all()
            for recept_info in recepts_info:
                recept = {}
                recept['name_prepations'] = Prepations.objects.get(name=recept_info.name_prepations).name                
                recept['name_patient'] = Patiens.objects.get(name=recept_info.name_patient).name
                recept['lastname_patient'] = Patiens.objects.get(lastname=recept_info.lastname_patient).lastname
                recept['patronymic_patient'] = Patiens.objects.get(patronymic=recept_info.patronymic_patient).patronymic                       
                login = Staff.objects.get(id=recept_info.id_staff).login_employee
                recept['name_employee'] = User.objects.get(username=login).first_name + ' ' + User.objects.get(username=login).last_name
                recept['date_issue'] =  recept_info.date_issue
                recepts.append(recept)
            seleted_recept = Recepts.objects.get(id=id_recepts)
            seleted_recept_for_templade = {}
            seleted_recept_for_templade['name_prepations'] = Prepations.objects.get(name=seleted_recept.name_prepations).name
            seleted_recept_for_templade['name_patient'] = Patiens.objects.get(name=seleted_recept.name_patient).name
            seleted_recept_for_templade['lastname_patient'] = Patiens.objects.get(lastname=seleted_recept.lastname_patient).lastname
            seleted_recept_for_templade['patronymic_patient'] = Patiens.objects.get(patronymic=seleted_recept.patronymic_patient).patronymic
            login = Staff.objects.get(id=seleted_recept.id_staff).login_employee
            seleted_recept_for_templade['name_employee'] = User.objects.get(username=login).first_name + ' ' + User.objects.get(username=login).last_name
            seleted_recept_for_templade['date_issue'] =  seleted_recept.date_issue
            flag_view_additional_info = True;
            return render(request, 'extract_app/recepts.html', {'recept':seleted_recept_for_templade, 
            'recepts':recepts,'flag_view_additional_info':flag_view_additional_info})
        else:
            auth.logout(request)
            return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')


# # def get_recept(request, id_recepts=1):
# #     if request.user.is_authenticated:
# #         type_user = Staff.objects.get(login_employee=request.session['login']).type_users
# #         if type_user == 'medico':
# #             recepts = []
# #             recepts_info = Recepts.objects.all()
# #             for recept_info in recepts_info:
# #                 recept = {}
# #                 recept['name_patients'] = Patiens.objects.get(id=recept_info.id_patiens).name
# #                 login = Staff.objects.get(id=recept_info.id_staff).login_employee
# #                 recept['name_employee'] =  User.objects.get(username=login).first_name + ' ' + User.objects.get(username=login).last_name
# #                 recept['date_issue'] =  recept_info.date_issue
# #                 recepts.append(recept)
# #             seleted_recept = Recepts.objects.get(id=id_recepts)
# #             seleted_recept_for_templade = {}
# #             seleted_recept_for_templade['name_patients'] = Patiens.objects.get(id=seleted_recept.id_patiens).name
# #             login = Staff.objects.get(id=seleted_recept.id_staff).login_employee
# #             seleted_recept_for_templade['name_employee'] = User.objects.get(username=login).first_name + ' ' + User.objects.get(username=login).last_name
            
# #             seleted_recept_for_templade['date_issue'] =  seleted_recept.date_issue
# #             flag_view_additional_info = True;
# #             return render(request, 'extract_app/recepts.html', {'recept':seleted_recept_for_templade, 
# #             'recepts':recepts,'flag_view_additional_info':flag_view_additional_info})
# #         else:
# #             auth.logout(request)
# #             return redirect('/logsys/login')
# #     else:
# #         return redirect('/logsys/login')



def new_recept(request):
    if request.is_ajax():            
        if request.method == 'GET':
            recept = Recepts.objects.filter(id_staff=request.GET['polis'])
            if len(patient) != 0:
                return HttpResponse('repit_polis', content_type='text/html')
            else:
                recept = Recepts(name_prepations=request.GET['name_prepations'],
                    name_patient=request.GET['name_patient'],
                    lastname_patient=request.GET['lastname_patient'],
                    patronymic_patient=request.GET['patronymic_patient'],
                    diagnos=request.GET['diagnos'],
                    date_issue=request.GET['date_issue'])
                patient.save()
                return HttpResponse('ok', content_type='text/html')
    else:
        return HttpResponse('no', content_type='text/html')