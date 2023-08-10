from django.contrib import admin
from . models import CustomUser, Department, Patient, Doctor, Appointment


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Department)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)

