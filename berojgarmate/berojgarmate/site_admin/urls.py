from django.urls import path , include
from .import views
from django.contrib import admin
from django.urls import path , include




urlpatterns = [
    
    path('',views.index_page, name='index'),
    path('/home',views.index_page, name='home'),

    path('/admin_signup', views.admin_signup,name="admin_signup"),

]
