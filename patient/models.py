from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ("male", "male"),
    ("female", "female"),
    ("rather not say", "rather not say"),
)

TIME_CHOICES = (
    ("morning", "11am"),
    ("noon", "12pm"),
    ("afternoon", "2pm"),
    ("evening", "4pm")
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
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default="rather not say")

    def __str__(self):
        return self.patient_name


class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.CharField(max_length=20, choices=DOCTORS, default="Dr. Oreste")
    date = models.CharField(max_length=20, choices=TIME_CHOICES, default="noon")

    def __str__(self):
        return "%s Your Appointment is Confirmed!" % self.patient_name
