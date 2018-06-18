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
from django.http import HttpResponse
import json

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
        global employee_id
        employee_id = Staff.objects.get(login_employee=request.session['login']).id
        if type_user == 'medico':
            recepts = []
            recepts_info = Recepts.objects.all()
            # staff_search_id = Staff.objects.all()

            for recept_info in recepts_info:
                recept = {}
                recept['id'] = Recepts.objects.get(id=recept_info.id).id
                recept['name_prepations'] = Prepations.objects.get(id=recept_info.id_prepations).name              
                recept['name_patient'] = Patiens.objects.get(id=recept_info.id_patiens).name
                recept['lastname_patient'] = Patiens.objects.get(id=recept_info.id_patiens).lastname
                recept['patronymic_patient'] = Patiens.objects.get(id=recept_info.id_patiens).patronymic                       
                recept['login_employee'] = Staff.objects.get(id=recept_info.id_staff).login_employee
                login = Staff.objects.get(id=recept_info.id_staff).login_employee
                recept['name_employee'] = User.objects.get(username=login).first_name + ' ' + User.objects.get(username=login).last_name
                recept['date_issue'] =  recept_info.date_issue
                recepts.append(recept)
                
            recepts.reverse()

            flag_view_additional_info = False;
            return render(request, 'extract_app/recepts.html', {'recepts':recepts, 
            'flag_view_additional_info':flag_view_additional_info,
            'list_prepations':Prepations.objects.all(),'list_patients':Patiens.objects.all(), 'employee_id':employee_id })
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
                recept['name_prepations'] = Prepations.objects.get(id=recept_info.id_prepations).name                 
                recept['name_patient'] = Patiens.objects.get(id=recept_info.id_patiens).name
                recept['lastname_patient'] = Patiens.objects.get(id=recept_info.id_patiens).lastname
                recept['patronymic_patient'] = Patiens.objects.get(id=recept_info.id_patiens).patronymic                       
                login = Staff.objects.get(id=recept_info.id_staff).login_employee
                recept['name_employee'] = User.objects.get(username=login).first_name + ' ' + User.objects.get(username=login).last_name
                recept['date_issue'] =  recept_info.date_issue
                recepts.append(recept)
            seleted_recept = Recepts.objects.get(id=id_recepts)
            seleted_recept_for_templade = {}
            seleted_recept_for_templade['name_prepations'] = Prepations.objects.get(id=seleted_recept.id_prepations).name
            seleted_recept_for_templade['name_patient'] = Patiens.objects.get(id=seleted_recept.id_patiens).name
            seleted_recept_for_templade['lastname_patient'] = Patiens.objects.get(id=seleted_recept.id_patiens).lastname
            seleted_recept_for_templade['patronymic_patient'] = Patiens.objects.get(id=seleted_recept.id_patiens).patronymic
            login = Staff.objects.get(id=seleted_recept.id_staff).login_employee
            seleted_recept_for_templade['name_employee'] = User.objects.get(username=login).first_name + ' ' + User.objects.get(username=login).last_name
            seleted_recept_for_templade['date_issue'] =  seleted_recept.date_issue
            flag_view_additional_info = True;
            recepts.reverse()
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



def recepts_search(request):
    type_user = Staff.objects.get(login_employee=request.session['login']).type_users
    if request.method == 'GET':
        flag_view_additional_info = False
        search_term = request.GET['search_term']
        recepts = []
        return_object = []
        recepts.extend(Prepations.objects.filter(name=search_term))
        recepts.extend(Prepations.objects.filter(type_prepations=search_term))
        recepts.extend(Prepations.objects.filter(form_release=search_term))
        for item in recepts:
            recept = {}
            recept['name_prepations'] = Recepts.objects.get(id_prepations=item.id).name
            recept['type_prepations'] = Prepations.objects.get(type_prepations=item.type_prepations).type_prepations
            recept['form_release'] = Prepations.objects.get(form_release=item.form_release).form_release
            return_object.append(recept)
# def recepts_search(request):
#     type_user = Staff.objects.get(login_employee=request.session['login']).type_users
#     if request.method == 'GET':
#         flag_view_additional_info = False
#         search_term = request.GET['search_term']
#         recepts = []
#         return_object = []
#         recepts.extend(Recepts.objects.filter(name_patient=search_term))
#         recepts.extend(Recepts.objects.filter(lastname_patient=search_term))
#         recepts.extend(Recepts.objects.filter(patronymic_patient=search_term))
#         recepts.extend(Recepts.objects.filter(name_prepations=search_term))
#         recepts.extend(Recepts.objects.filter(date_issue=search_term))
#         recepts.extend(User.objects.filter(first_name=search_term))
#         for item in recepts:
#             recept = {}
#             recept['id'] = Recepts.objects.get(id=item.id).id
#             recept['name_patient'] = Recepts.objects.get(name_patient=item.name_patient).name_patient
#             recept['lastname_patient'] = Recepts.objects.get(lastname_patient=item.lastname_patient).lastname_patient
#             recept['patronymic_patient'] = Recepts.objects.get(patronymic_patient=item.patronymic_patient).patronymic_patient
#             recept['name_prepations'] = Prepations.objects.get(name=item.name_prepations).name
#             recept['date_issue'] =  item.date_issue
#             return_object.append(recept)
#         recepts = []
#         recepts.extend(Prepations.objects.filter(maker=search_term))
#         recepts.extend(Prepations.objects.filter(form_release=search_term))       
#         for item in recepts:
#                 recept = {}
#                 recept['id'] = item.id
#                 recept['name_patient'] = item.name_patient
#                 recept['lastname_patient'] = item.lastname_patient
#                 recept['patronymic_patient'] = item.patronymic_patient
#                 recept['name_prepations'] = item.name
#                 recept['date_issue'] = item.date_issue
#                 return_object.append(recept)

        return render(request, 'extract_app/recepts.html', 
            {'recepts':return_object, 'flag_view_additional_info':flag_view_additional_info})
    else:
        return render(request, 'extract_app/recepts.html', 
            {'flag_view_additional_info':flag_view_additional_info})

def delet_recept(request, id_recept=1):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        login_employee = Staff.objects.get(login_employee=request.session['login']).login_employee
        user_id = Staff.objects.get(login_employee=request.session['login']).id
        if type_user == 'medico':     
            try:
                recept = Recepts.objects.get(id=id_recept)
                recept_delete = Recepts.objects.get(id=id_recept).id_staff
                if recept_delete == user_id:
                    recept.delete()
                else:
                    show_red_delete = True

                recepts = Recepts.objects.all()
                flag_view_additional_info = False
                return render(request, 'extract_app/recepts.html', {'recepts':recepts, 'flag_view_additional_info':flag_view_additional_info, 
                'show_red_delete':show_red_delete})
            
            except Recepts.DoesNotExist:
                recepts = Recepts.objects.exclude(id=id_recept)
                return render(request, 'extract_app/recepts.html', {'recepts':recepts})
                
            else:
                auth.logout(request)
                return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')

def new_recept(request):
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    if request.is_ajax():            
        if request.method == 'GET':
            # recept = Recepts.objects.filter(id=request.GET['id'])
            # if len(patient) != 0:
            #     return HttpResponse('repit_polis', content_type='text/html')
            # else:
                recept = Recepts(id_prepations=request.GET['id_prepation'],
                    id_patiens=request.GET['id_patient'],
                    id_staff = employee_id,
                    date_issue = request.GET['date_issue'],)                   
                recept.save()
                return HttpResponse(json.dumps({
                    "status_responce": "ok", 
                    }),
                    content_type="application/json")
    else:
        return HttpResponse('no', content_type='text/html')