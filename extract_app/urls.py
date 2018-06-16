from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^new_recept/$', views.new_recept, name='new_recept'),

    url(r'^main$', views.get_main_page, name='get_main_page'),

    url(r'^recepts/$', views.get_recepts_page, name='get_recepts_page'),
    url(r'^recepts/(?P<id_recepts>\d+)', views.get_recept, name='get_recept'),

]