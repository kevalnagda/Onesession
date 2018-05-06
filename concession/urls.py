from django.conf.urls import url
from . import views

app_name = 'concession'

urlpatterns = [
    url(r'^login/', views.login_user, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^index/', views.index, name='index'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^conform/', views.create_conform, name='create_conform'),
    url(r'^details/', views.details, name='details'),
    url(r'^info/(?P<form_id>[0-9]+)', views.info, name='info'),
    url(r'^status/(?P<form_id>[0-9]+)', views.Formstatus, name='status'),
    url(r'^change/', views.change, name='change'),
    url(r'^edit/', views.edit, name='edit'),
    url(r'^editinfo/(?P<form_id>[0-9]+)', views.editinfo, name='editinfo'),
    url(r'^userstatus/(?P<form_id>[0-9]+)', views.userstatus, name='userstatus'),
]
