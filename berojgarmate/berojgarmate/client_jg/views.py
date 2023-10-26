from django.shortcuts import render
from . models import *

# Create your views here.
def client_jg_signup(request):

    jg_first_name = request.POST.get('form3Example1m')
    jg_last_name = request.POST.get('form3Example1n')
    jg_city = request.POST.get('form3Example1m1')
    jg_state = request.POST.get('form3Example1n1')
    jg_email_id = request.POST.get('form3Example8')
    jg_gender = request.POST.get('form3Example1ngen')
    jg_dob = request.POST.get('form3Example9')

    jg_edu = request.POST.get('form3Example99')
    jg_phno = request.POST.get('form3Example97')


    sql = job_giver_details(first_name=jg_first_name, last_name=jg_last_name, city=jg_city, state=jg_state,Email_id=jg_email_id, gender=jg_gender, date_of_birth=jg_dob, education=jg_edu,mobile_number=jg_phno)
    sql.save()
    # print(jg_edu,jg_last_name,jg_first_name)
    return render(request,"client_jg/html/client_jg_signup.html")





def client_jg_signin(request):
    print("i am views of jg")



def client(request):
    return render(request, "client_jg/html/client.html")
