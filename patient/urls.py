from django.urls import path
from .views import AppointmentListView, AppointmentCreateView
from . import views

urlpatterns = [
    path('', views.home, name="patient-home"),
    path('about/', views.about, name ='patient-about'),
    path("appointment", AppointmentListView.as_view(), name="patient-appointment"),
    path("createappointment/", AppointmentCreateView.as_view(), name="patient-createappointment")
    # path('doctor/', views.doctor, name ='patient-doctor')
]
