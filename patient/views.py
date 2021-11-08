from django.shortcuts import render, redirect, HttpResponse, reverse
from .models import Patient, Appointment
from .forms import AppointmentForm, PatientForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import View
from django.contrib import messages

# Create your views here.
class AppointmentListView(ListView):
    model = Appointment
    template_name = "patient/appointment.html"
    context_object_name = "appointment"

class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ['patient', 'doctor', 'date']
    template_name = "patient/createappointment.html"
    success_url = "/"

def home(request):
    context = {
        'posts': Patient.objects.all(),
    }
    return render(request, 'patient/home.html', context)

def about(request):
    return render(request, 'patient/about.html', {'title':'About Afya'})

def appointment(request):
    context = {
        'posts': Appointment.objects.all()
    }
    return render(request, 'patient/appointment.html', context)


def doctor(request):
    context = {
        'posts': Doctor.objects.all()
    }
    return render(request, 'patient/doctor.html', context)
