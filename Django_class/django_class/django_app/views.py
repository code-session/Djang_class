from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'frontend_files/form.htm')




def index(request):
    return HttpResponse("hyy this is index pageg gfdsgfdgfdg gdfgdf")
