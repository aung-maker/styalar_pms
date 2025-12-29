from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Source)
admin.site.register(Reservation)
admin.site.register(ReservationRequest)