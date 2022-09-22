
from django.shortcuts import render, HttpResponse , redirect
from .forms import *

from .models import *

# Create your views here.


def home (request):
    student=Students_info.objects.all()
    if  request.method == "POST":
        fm= input_form(request.POST)
        if fm.is_valid:
            fm.save()
            fm= input_form()

    else:
        fm= input_form()
    
    
    
    context={
        'students':student,
        'form':fm,
    }

    return render (request,'table.html',context)

def Delete_data(request, id ):
    student=Students_info.objects.get(id=id)
    student.delete()
   


    return redirect ('/')


def edit_data(request,id):

    if  request.method == 'POST':
        ed=Students_info.objects.get(id=id)
        fm=edit_form(request.POST,instance=ed)
        if  fm.is_valid:
            fm.save()
            
    else:
        ed=Students_info.objects.get(id=id)
        fm=edit_form(instance=ed)
        
    
    return render(request,'edit.html',{'form':fm})


def details_data(request,id):
    detail=Students_info.objects.filter(id=id)
    context={'d':detail}
    return render(request,'details.html',context)


def singup(request):
    return render (request,'singup.html')
     