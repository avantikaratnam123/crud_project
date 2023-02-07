
from django.urls import path,include
from . import views
from  django.urls import re_path

urlpatterns = [
    
    path('',views.index),
    path("login/",views.login),
    path("registration/",views.registration),
    path("welcome/",views.welcome),
    path("Login_form/",views.Login_form),
    path('update_view/<int:uid>/',views.update_view),
    path('update_form_data/',views.update_form_data),
    path('table/',views.table),
    re_path(r'^delete/(?P<pk>[0-9]+)/$',views.delete,name="delete")
]
