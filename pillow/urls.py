from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import search
from .views import filter_doctors
from .views import doctor_list

urlpatterns = [
   ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns = [
    path('search/', search, name='search'),
]


urlpatterns = [
    path('doctors/', filter_doctors, name='filter_doctors'),
]

urlpatterns = [
    path('doctors/', doctor_list, name='doctor_list'),
]
