from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^main$', views.get_main_page, name='get_main_page'),
    url(r'^archive$', views.get_archive_page, name='get_archive_page'),
]