from django.shortcuts import render, redirect, HttpResponse, reverse
from .models import Patient, Appointment
from .forms import AppointmentForm, PatientForm, AppointmentUpdateForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import View
from django.contrib import messages

# Create your views here.
class AppointmentListView(ListView):
    model = Appointment
    template_name = "patient/appointment.html"
    context_object_name = "appointment"


def createappointment(request):
    form = PatientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/createappointment')
    context = {
        'form': form
    }
    return render(request, 'patient/createappointment.html', context)

def appointment(request):
    header = 'List of Appointments'
    queryset = Appointment.objects.all()
    context = {
        "header" : header,
        "queryset": queryset,
    }
    return render(request, 'patient/appointment.html', context)


def update_appointment(request, pk):
    queryset = Appointment.objects.all()
    form = AppointmentUpdateForm(instance = queryset)
    if request.method == 'POST':
        form = AppointmentUpdateForm(request.POST, instance = queryset)
        if form.is_valid():
            form.save()
            return redirect('/appointment')

    context = {
        'form': form
    }
    return render(request, 'patient/appointment.html', context)

class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ['patient','doctor', 'date']
    template_name = "patient/createappointment.html"
    success_url = "/"


def home(request):
    context = {
        'posts': Patient.objects.all(),
    }
    return render(request, 'patient/home.html', context)


def about(request):
    return render(request, 'patient/about.html', {'title':'About Afya'})


def doctor(request):
    context = {
        'posts': Doctor.objects.all()
    }
    return render(request, 'patient/doctor.html', context)
