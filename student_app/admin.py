from django.contrib import admin
from .models import StudentDetails, Location
from.models import  Location,PhoneNumber,ProgramInfo,CampaignDetails
# Register your models here.
admin.site.register(StudentDetails)
admin.site.register(Location)
admin.site.register(PhoneNumber)
admin.site.register(ProgramInfo)
admin.site.register(CampaignDetails)