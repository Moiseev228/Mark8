from django.conf.urls import url
from . import views

urlpatterns = [

    
    url(r'^new_employee/$', views.new_employee, name='new_employee'),

    url(r'^main/$', views.get_main_page, name='get_main_page'),

    url(r'^staff/search/$', views.staff_search, name='staff_search'),
    url(r'^staff/$', views.get_staff_page, name='get_staff_page'),
    url(r'^staff/(?P<id_employees>\d+)', views.get_employee, name='get_employee'),
    url(r'^delete-employee/(?P<id_employees>\d+)', views.delet_employee, name='delet_employee'),

    url(r'^preparations/search/$', views.preparations_search, name='preparations_search'),
    url(r'^preparations/$', views.get_preparations_page, name='get_preparations_page'),
    url(r'^preparations/(?P<id_preparations>\d+)', views.get_preparation, name='get_preparation'),
    url(r'^delete-prepation/(?P<id_preparations>\d+)', views.delet_preparation, name='delet_preparation'),

    url(r'^recepts/search/$', views.recepts_search, name='recepts_search'),
    url(r'^recepts/$', views.get_recepts_page, name='get_recepts_page'),
    url(r'^recepts/(?P<id_recepts>\d+)', views.get_recept, name='get_recept'),
    url(r'^delete-recept/(?P<id_recept>\d+)', views.delet_recept, name='delet_recept'),

    url(r'^patients/search/$', views.patients_search, name='patients_search'),
    url(r'^patients/$', views.get_patients_page, name='get_patients_page'),
    url(r'^patients/(?P<id_patients>\d+)', views.get_patient, name='get_patient'),
    url(r'^delete-patient/(?P<id_patien>\d+)', views.delet_patient, name='delet_patient'),
    
]