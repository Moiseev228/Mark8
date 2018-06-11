from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^new_patient/$', views.new_patient, name='new_patient'),

    url(r'^main/$', views.get_main_page, name='get_main_page'),

    url(r'^preparations/$', views.get_preparations_page, name='get_preparations_page'),
    url(r'^preparations/(?P<id_preparations>\d+)', views.get_preparation, name='get_preparation'),
    
    url(r'^patients/$', views.get_patients_page, name='get_patients_page'),
    url(r'^patients/(?P<id_patients>\d+)', views.get_patient, name='get_preparation'),
]