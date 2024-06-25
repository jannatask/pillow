from django.shortcuts import render
from rest_framework import viewsets
from .models import Doctor
from .serializers import DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


def search(request):
    query = request.GET.get('q', '')
    if query:
        doctors = Doctor.objects.filter(name__icontains=query)
    else:
        doctors = Doctor.objects.all()
    return render(request, 'doctors/search_results.html', {'doctors': doctors})


def filter_doctors(request):
    specialty = request.GET.get('specialty')
    available = request.GET.get('available')

    doctors = Doctor.objects.all()

    if specialty:
        doctors = doctors.filter(specialty__iexact=specialty)
    if available:
        doctors = doctors.filter(available=True if available == 'true' else False)

    return render(request, 'doctors/doctor_list.html', {'doctors': doctors})




