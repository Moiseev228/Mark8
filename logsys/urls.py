from django.conf.urls import url
from logsys import views
from django.urls import include

urlpatterns = [
    url(r'^login', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),

]