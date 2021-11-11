from django import forms
from .models import Appointment, Patient


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class AppointmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
