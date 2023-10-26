from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # path('', views.index_page),
    path('client_js_signup/',views.client_js_signup, name='client_js_signup'),
    path('client_js_signin/',views.client_js_signin, name='client_js_signin'),
    path('client_js_index/',views.client_js_index, name='client_js_index'),
    path('client_js_login/',views.client_js_login, name='login'),



]
