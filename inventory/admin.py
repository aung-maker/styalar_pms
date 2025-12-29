from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Property)
admin.site.register(Zone)
admin.site.register(Building)
admin.site.register(Floor)
admin.site.register(Exposure)
admin.site.register(Attribute)
admin.site.register(BedType)
admin.site.register(RoomType)
admin.site.register(RoomTypeBed)
admin.site.register(Room)
admin.site.register(AddOnItem)