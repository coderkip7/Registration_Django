from django.shortcuts import render
from django.http import HttpResponse
from .models import People
#Create your views here.

def home(request):
    return render(request, 'index.html')

def insert(request):
    if request.method == "POST":
        name=request .POST.get('name')
        school=request .POST.get('school')
        email=request .POST.get('email')


        person= People(name=name, email=email, school=school)
        person.save()


        return HttpResponse ("Success")
    # return render(request,'index.html')

def people(request):
    data = People.objects.all()
    return render(request, 'people.html', {"data": data})

def delete(request, id):
    dd = People.objects.get(id=id)
    dd.delete()

    return HttpResponse("Delete successful")


def update(request, id):
    l = People.objects.get(id=id)

    return render(request, "edit.html", {"l": l})