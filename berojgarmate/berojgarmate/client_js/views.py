from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,HttpResponse,redirect
from client_jg.models import job_giver_details
from . models import job_seeker_details



# Create your views here.
def client_js_signup(request):


    js_first_name = request.POST.get('form3Example1m')
    js_last_name = request.POST.get('form3Example1n')
    js_city = request.POST.get('form3Example1m1')
    js_state = request.POST.get('form3Example1n1')
    js_email_id = request.POST.get('form3Example8')
    js_gender = request.POST.get('form3Example1ngen')
    js_dob = request.POST.get('form3Example9')

    js_edu = request.POST.get('form3Example99')
    js_phno = request.POST.get('form3Example97')


    sql = job_seeker_details(first_name=js_first_name, last_name=js_last_name, city=js_city, state=js_state,Email_id=js_email_id, gender=js_gender, date_of_birth=js_dob, education=js_edu,mobile_number=js_phno)
    sql.save()
    print(js_edu,js_last_name,js_first_name)
    return render(request,"client_js/html/client_js_signup.html")


def client_js_index(request):
    crse = job_giver_details.objects.all()
    return render(request, "client_js/html/client_js_index.html",{'crse':crse})



def client_js_signin(request):
    return render(request, "client_js/html/client_js_login.html")
    # return redirect('client_js_index')

def client_js_login(request):
    print("hello")
    pass


