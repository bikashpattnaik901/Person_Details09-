from django.shortcuts import render
from .models  import Employee


def details(request):
    q = Employee.objects.order_by('age')[4:6]
    return render(request,'techapp/index.html',{'q':q})
    

