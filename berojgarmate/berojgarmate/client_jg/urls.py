from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [


    # path('', views.index_page),
    path('client_jg_signup/',views.client_jg_signup, name='client_jg_signup'),
    path('client_jg_signin/',views.client_jg_signin, name='client_jg_signin'),
    path('client/', views.client, name="client"),



]
