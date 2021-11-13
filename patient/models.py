from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Rather not say", "Rather not say"),
)

TIME_CHOICES = (
    ("Morning", "11 AM"),
    ("Noon", "12 PM"),
    ("Afternoon", "2 PM"),
    ("Evening", "4 PM")
)

DOCTORS = (
    ("Dr. Martin", "Dr. Martin"),
    ("Dr. Mutembei", "Dr. Mutembei"),
    ("Dr. Steve", "Dr. Steve"),
    ("Dr. Ther", "Dr. Ther"),
    ("Dr. Oreste", "Dr. Oreste")
)

# Create your models here.


class Patient(models.Model):
    patient_name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient_name


class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.CharField(max_length=20, choices=DOCTORS, default="Dr. Oreste")
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default="Rather not say")
    time_of_day = models.CharField(max_length=20, choices=TIME_CHOICES, default="Noon")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.patient
