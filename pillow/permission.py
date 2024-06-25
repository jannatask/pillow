from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

class ClinicPermission(Permission):
    class Meta:
        verbose_name = 'Clinic Permission'
        verbose_name_plural = 'Clinic Permissions'


content_type = ContentType.objects.get_for_model(MedicalRecord)
permission = ClinicPermission.objects.create(
    codename='view_medical_records',
    name='Can view medical records',
    content_type=content_type,
)
