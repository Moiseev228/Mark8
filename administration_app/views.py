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
                ssued['name_prepations'] = Prepations.objects.get(name=item.name_prepations).name
                ssued['name_patient'] = Patiens.objects.get(name=item.name_patient).name
                ssued['lastname_patient'] = Patiens.objects.get(lastname=item.lastname_patient).lastname
                ssued['patronymic_patient'] = Patiens.objects.get(patronymic=item.patronymic_patient).patronymic
                ssued['date_issue'] = item.date_issue
                return_objects_employee['prescriptions_issued'].append(ssued)
            return_objects_staff.reverse()
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
            return_object_preparations = []
            preparations = Prepations.objects.all()
            for item in preparations:
                prepation = {}
                prepation['id'] = item.id
                prepation['name'] = item.name
                prepation['type_prepations'] = item.type_prepations
                prepation['maker'] = item.maker
                prepation['form_release'] = item.form_release
                return_object_preparations.append(prepation)
            flag_view_additional_info = False
            return_object_preparations.reverse()
            return render(request, 'administration_app/preparations.html', {'preparations':return_object_preparations, 'flag_view_additional_info':flag_view_additional_info})
        else:
            auth.logout(request)
            return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')

def get_preparation(request, id_preparations=1):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'administration':
            return_object_preparations = []
            preparations = Prepations.objects.all()
            for item in preparations:
                prepation = {}
                prepation['id'] = item.id
                prepation['name'] = item.name
                prepation['type_prepations'] = item.type_prepations
                prepation['maker'] = item.maker
                prepation['form_release'] = item.form_release
                return_object_preparations.append(prepation)
            return_object_preparations.reverse()
            flag_view_additional_info = True
            return render(request, 'administration_app/preparations.html', {'prepation':Prepations.objects.get(id=id_preparations), 
            'preparations':return_object_preparations,'flag_view_additional_info':flag_view_additional_info})
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
                recept['id'] = Recepts.objects.get(id=recept_info.id).id
                recept['name_prepations'] = Prepations.objects.get(name=recept_info.name_prepations).name                
                recept['name_patient'] = Patiens.objects.get(name=recept_info.name_patient).name
                recept['lastname_patient'] = Patiens.objects.get(lastname=recept_info.lastname_patient).lastname
                recept['patronymic_patient'] = Patiens.objects.get(patronymic=recept_info.patronymic_patient).patronymic                       
                login = Staff.objects.get(id=recept_info.id_staff).login_employee
                recept['name_employee'] = User.objects.get(username=login).first_name + ' ' + User.objects.get(username=login).last_name
                recept['date_issue'] =  recept_info.date_issue
                recepts.append(recept)
                recepts.reverse()
                print(recept)
            flag_view_additional_info = False;
            return render(request, 'administration_app/recepts.html', {'recepts':recepts, 'flag_view_additional_info':flag_view_additional_info})
        else:
            auth.logout(request)
            return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')

# # def get_recepts_page(request):
# #     if request.user.is_authenticated:
# #         type_user = Staff.objects.get(login_employee=request.session['login']).type_users
# #         if type_user == 'administration':
# #             recepts = []
# #             recepts_info = Recepts.objects.all()
# #             for recept_info in recepts_info:
# #                 recept = {}
# #                 recept['name_patients'] = Patiens.objects.get(id=recept_info.id_patiens).name
# #                 login = Staff.objects.get(id=recept_info.id_staff).login_employee
# #                 recept['name_employee'] = User.objects.get(username=login).first_name + ' ' + User.objects.get(username=login).last_name
# #                 recept['date_issue'] =  recept_info.date_issue
# #                 recepts.append(recept)
# #                 print(recept)
# #             flag_view_additional_info = False;
# #             return render(request, 'administration_app/recepts.html', {'recepts':recepts, 'flag_view_additional_info':flag_view_additional_info})
# #         else:
# #             auth.logout(request)
# #             return redirect('/logsys/login')
# #     else:
# #         return redirect('/logsys/login')




def get_recept(request, id_recepts=1):
    
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'administration':
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
                recepts.reverse()
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
            return render(request, 'administration_app/recepts.html', {'recept':seleted_recept_for_templade, 
            'recepts':recepts,'flag_view_additional_info':flag_view_additional_info})
        else:
            auth.logout(request)
            return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')

# # def get_recept(request, id_recepts=1):
# #     if request.user.is_authenticated:
# #         type_user = Staff.objects.get(login_employee=request.session['login']).type_users
# #         if type_user == 'administration':
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
# #             return render(request, 'administration_app/recepts.html', {'recept':seleted_recept_for_templade, 
# #             'recepts':recepts,'flag_view_additional_info':flag_view_additional_info})
# #         else:
# #             auth.logout(request)
# #             return redirect('/logsys/login')
# #     else:
# #         return redirect('/logsys/login')

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
            try:
                return render(request, 'administration_app/patients.html', {'patien':Patiens.objects.get(id=id_patients), 
                'patiens':patiens,'flag_view_additional_info':flag_view_additional_info})
            except DoesNotExist:
                return render(request, 'administration_app/patients.html', { 'patiens':patiens,'flag_view_additional_info':flag_view_additional_info})               
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
            
   
def preparations_search(request):
    if request.method == 'GET':
        flag_view_additional_info = False
        search_term = request.GET['search_term']
        prepations = []
        return_object = []
        prepations.extend(Prepations.objects.filter(name=search_term))
        prepations.extend(Prepations.objects.filter(type_prepations=search_term))
        for item in prepations:
            preparation = {}
            preparation['id'] = Prepations.objects.get(name=item.name).id
            preparation['name'] = Prepations.objects.get(name=item.name).name
            preparation['type_prepations'] = Prepations.objects.get(name=item.name).type_prepations
            preparation['maker'] = Prepations.objects.get(name=item.name).maker
            preparation['form_release'] = Prepations.objects.get(name=item.name).form_release
            return_object.append(preparation)
        prepations = []
        prepations.extend(Prepations.objects.filter(maker=search_term))
        prepations.extend(Prepations.objects.filter(form_release=search_term))
        for item in prepations:
                preparation = {}
                preparation['id'] = item.id
                preparation['name'] = item.name
                preparation['type_prepations'] = item.type_prepations
                preparation['maker'] = item.maker
                preparation['form_release'] = item.form_release
                return_object.append(preparation)

        return render(request, 'administration_app/preparations.html', 
            {'preparations':return_object, 'flag_view_additional_info':flag_view_additional_info})
    else:
        return render(request, 'administration_app/preparations.html', 
            {'flag_view_additional_info':flag_view_additional_info})

def patients_search(request):
    if request.method == 'GET':
        flag_view_additional_info = False
        search_term = request.GET['search_term']
        patients = []
        return_object = []
        patients.extend(Patiens.objects.filter(name=search_term))
        patients.extend(Patiens.objects.filter(lastname=search_term))
        patients.extend(Patiens.objects.filter(patronymic=search_term))
        for item in patients:
            patient = {}
            patient['id'] = Patiens.objects.get(name=item.name).id
            patient['name'] = Patiens.objects.get(name=item.name).name
            patient['lastname'] = Patiens.objects.get(name=item.name).lastname
            patient['patronymic'] = Patiens.objects.get(name=item.name).patronymic
            patient['address'] = Patiens.objects.get(name=item.name).address
            patient['polis'] = Patiens.objects.get(name=item.name).polis
            patient['phone'] = Patiens.objects.get(name=item.name).phone
            patient['date_of_birth'] = Patiens.objects.get(name=item.name).date_of_birth
            patient['sector'] = Patiens.objects.get(name=item.name).sector
            patient['Recording_date'] = Patiens.objects.get(name=item.name).Recording_date
            return_object.append(patient)
        patients = []
        patients.extend(Patiens.objects.filter(address=search_term))
        patients.extend(Patiens.objects.filter(polis=search_term))
        patients.extend(Patiens.objects.filter(phone=search_term))
        patients.extend(Patiens.objects.filter(date_of_birth=search_term))
        patients.extend(Patiens.objects.filter(sector=search_term))
        patients.extend(Patiens.objects.filter(Recording_date=search_term))
        for item in patients:
            patient = {}
            patient['id'] = item.id
            patient['name'] = item.name
            patient['lastname'] = item.lastname
            patient['address'] = item.address
            patient['polis'] = item.polis
            patient['phone'] = item.phone
            patient['date_of_birth'] = item.date_of_birth
            patient['sector'] = item.sector
            patient['Recording_date'] = item.Recording_date
            return_object.append(patient)

        return render(request, 'administration_app/patients.html', 
            {'patiens':return_object, 'flag_view_additional_info':flag_view_additional_info})
    else:
        return render(request, 'administration_app/patients.html', 
            {'flag_view_additional_info':flag_view_additional_info})    
        
def recepts_search(request):
    type_user = Staff.objects.get(login_employee=request.session['login']).type_users
    if request.method == 'GET':
        flag_view_additional_info = False
        search_term = request.GET['search_term']
        recepts = []
        return_object = []
        recepts.extend(Recepts.objects.filter(name_patient=search_term))
        recepts.extend(Recepts.objects.filter(lastname_patient=search_term))
        recepts.extend(Recepts.objects.filter(patronymic_patient=search_term))
        recepts.extend(Recepts.objects.filter(name_prepations=search_term))
        recepts.extend(Recepts.objects.filter(date_issue=search_term))
        recepts.extend(User.objects.filter(first_name=search_term))
        for item in recepts:
            recept = {}
            recept['id'] = Recepts.objects.get(id=item.id).id
            recept['name_patient'] = Recepts.objects.get(name_patient=item.name_patient).name_patient
            recept['lastname_patient'] = Recepts.objects.get(lastname_patient=item.lastname_patient).lastname_patient
            recept['patronymic_patient'] = Recepts.objects.get(patronymic_patient=item.patronymic_patient).patronymic_patient
            recept['name_prepations'] = Prepations.objects.get(name=item.name_prepations).name
            recept['date_issue'] =  item.date_issue
            return_object.append(recept)
        recepts = []
        recepts.extend(Prepations.objects.filter(maker=search_term))
        recepts.extend(Prepations.objects.filter(form_release=search_term))       
        for item in recepts:
                print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
                print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
                recept = {}
                recept['id'] = item.id
                recept['name_patient'] = item.name_patient
                recept['lastname_patient'] = item.lastname_patient
                recept['patronymic_patient'] = item.patronymic_patient
                recept['name_prepations'] = item.name
                recept['date_issue'] = item.date_issue
                return_object.append(recept)

        return render(request, 'administration_app/recepts.html', 
            {'recepts':return_object, 'flag_view_additional_info':flag_view_additional_info})
    else:
        return render(request, 'administration_app/recepts.html', 
            {'flag_view_additional_info':flag_view_additional_info})

def delet_employee(request, id_employees=1):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'administration':    
            try:
                return_objects = []
                delete = Staff.objects.get(id=id_employees)
                delete.delete()
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
                return render(request, 'administration_app/staff.html', {'staff':return_objects, 'flag_view_additional_info':flag_view_additional_info})
            except Staff.DoesNotExist:
                return_objects = []
                staff = Staff.objects.exclude(id=id_employees)
                for item in staff:
                    employee = {}
                    employee['id'] = item.id
                    name_employee = User.objects.get(username=item.login_employee).first_name + ' ' + User.objects.get(username=item.login_employee).last_name
                    employee['name'] = name_employee
                    employee['post'] = item.post
                    employee['specialization'] = item.specialization
                    return_objects.append(employee)
                return render(request, 'administration_app/staff.html', {'staff':return_objects,})
                # return render(request, 'administration_app/main.html', {})
            else:
                auth.logout(request)
                return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')

def delet_patient(request, id_patien=1):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'administration':    
            try:
                delete = Patiens.objects.get(id=id_patien)
                delete.delete()
                patiens = Patiens.objects.all()
                flag_view_additional_info = False
                return render(request, 'administration_app/patients.html', {'patiens':patiens, 'flag_view_additional_info':flag_view_additional_info})
            except Patiens.DoesNotExist:
                patiens = Patiens.objects.exclude(id=id_patien)
                return render(request, 'administration_app/patients.html', {'patiens':patiens,})
            else:
                auth.logout(request)
                return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')

        
def delet_preparation(request, id_preparations=1):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'administration':    
            try:
                delete = Prepations.objects.get(id=id_preparations)
                delete.delete()
                # preparations = Prepations.objects.exclude(id=id_preparations)
                preparations = Prepations.objects.all()
                flag_view_additional_info = False
                return render(request, 'administration_app/preparations.html', {'preparations':preparations, 'flag_view_additional_info':flag_view_additional_info})
            except Prepations.DoesNotExist:
                preparations = Prepations.objects.exclude(id=id_preparations)
                return render(request, 'administration_app/preparations.html', {'preparations':preparations})
            else:
                auth.logout(request)
                return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')
       
       
def delet_recept(request, id_recept=1):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'administration':    
            try:
                delete = Recepts.objects.get(id=id_preparations)
                delete.delete()
                recepts = Recepts.objects.all()
                flag_view_additional_info = False
                return render(request, 'administration_app/recepts.html', {'recepts':recepts, 'flag_view_additional_info':flag_view_additional_info})
            except Recepts.DoesNotExist:
                recepts = Recepts.objects.exclude(id=id_recept)
                return render(request, 'administration_app/recepts.html', {'recepts':recepts})
            else:
                auth.logout(request)
                return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')
        