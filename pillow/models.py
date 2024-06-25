from django.db import models
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Doctor

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='doctors_photos/')
    specialty = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


def doctor_list(request):
    doctor_list = Doctor.objects.all()
    paginator = Paginator(doctor_list, 10) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'doctors/doctor_list.html', {'page_obj': page_obj})


class PatientRecord(models.Model):
    ...
    class Meta:
        permissions = (
            ("view_patientrecord", "Can view patient record"),
            ("edit_patientrecord", "Can edit patient record"),
        )
