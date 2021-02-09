from django.shortcuts import render
from django.http import HttpResponse
from .models import contact_form


def home(request):
    if request.method == "POST":
        Name = request.POST["willersname"]
        Mobile_number = request.POST["mnumber"]
        Addrs = request.POST["address"]
        Email = request.POST["email"]
        State = request.POST["state"]
        City = request.POST["city"]
        Qualiification = request.POST["qualification"]
        Interst_Area = request.POST["interst_Area"]
        Age = request.POST["age"]
        Instgram_Id = request.POST["INSTAGRAM_ID"]
        Blood_Group = request.POST["bloodgroup"]
        Whyjoin = request.POST["joinyouth"]
        contact_form.objects.create(name=Name, number=Mobile_number, address=Addrs, gmail=Email, Age=Age,
                                    QUALIFICATON=Qualiification, City=City, Blood_group=Blood_Group, INSTAGRAM_ID=Instgram_Id, JOIN_YW=Whyjoin)
        print("form is submitted")
    else:
        data = contact_form.objects.all()

    return render(request, 'frontend_files/home.htm', {"data": data})


def index(request):
    return HttpResponse("hyy this is index pageg gfdsgfdgfdg gdfgdf")
