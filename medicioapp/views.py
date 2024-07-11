from django.shortcuts import render, redirect

from medicioapp.form import AppointForm
from medicioapp.models import Contact, Appoint, Branch, Product
from medicioapp.form import AppointForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def starter(request):
    return render(request, 'starter-page.html')


def about(request):
    return render(request, 'about.html')


def doctors(request):
    return render(request, 'doctors.html')


def departments(request):
    return render(request, 'departments.html')


def contacts(request):
    #return render(request,'contacts.html')
    if request.method == 'POST':
        all = Contact(name=request.POST['name'],
                      email=request.POST['email'],
                      phone=request.POST['phone'],
                      message=request.POST['message'],
                      )
        all.save()
        return redirect('/contacts')
    else:
        return render(request, 'contacts.html')


def appoint(request):
    if request.method == 'POST':
        myappointments = Appoint(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            message=request.POST['message'],
            date=request.POST['date'],
            department=request.POST['department'],
            doctor=request.POST['doctor'],
        )

        myappointments.save()
        return redirect('/show')
    else:
        return render(request, 'appointment.html')


def branch(request):
    if request.method == 'POST':
        over = Branch(name=request.POST['name'],
                      email=request.POST['email'],
                      location=request.POST['location'],
                      manager=request.POST['manager'],
                      )

        over.save()
        return redirect('/branch')
    else:
        return render(request, 'branch.html')

def show(request):
    information = Appoint.objects.all()
    return render(request,'show.html',{'data':information})

def delete(request,id):
    myappointments = Appoint.objects.get(id = id)
    myappointments.delete()
    return redirect('/show')

def edit(request,id):
    appointment = Appoint.objects.get(id = id)
    return render(request,'edit.html',{'x':appointment})

def update(request,id):
    if request.method == 'POST':
        appointment = Appoint.objects.get(id = id)
        form = AppointForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('/show')
        else:
            return render(request,'edit.html')
    else:
        return render(request,'edit.html')

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')