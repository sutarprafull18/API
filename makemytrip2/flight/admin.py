from django.contrib import admin
from .models import FlightDetailsModel
# Register your models here.

class FlightDetailsAdmin(admin.ModelAdmin):
    list_display = ['fname', 'fdate', 'ffare', 'fstart', 'fend']

admin.site.register(FlightDetailsModel,FlightDetailsAdmin)