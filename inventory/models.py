from django.db import models

# Create your models here.
class Property(models.Model):
    name = models.CharField()
    
    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"
        
    def __str__(self):
        return self.name

class Zone(models.Model):
    name = models.CharField(max_length=255)
    property = models.ForeignKey(Property,on_delete=models.CASCADE,related_name='zones',null=True)
    
    def __str__(self):
        return self.name
    
class Building(models.Model):
    name = models.CharField(max_length=255)
    property = models.ForeignKey(Property,on_delete=models.CASCADE,related_name='buildings',null=True)
    zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True, blank=True, related_name='buildings')
    def __str__(self):
        return self.name

class Floor(models.Model):
    no = models.IntegerField()
    name = models.CharField(max_length=255,blank=True,null=True)
    property = models.ForeignKey(Property,on_delete=models.CASCADE,related_name='floors',null=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='floors', null=True)
    def __str__(self):
        return self.name
    
class Exposure(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='images/icons/',blank=True,null=True)
    slug = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Attribute(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='images/icons/',blank=True,null=True)
    slug = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class BedType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to='images/icons/',blank=True,null=True)
    slug = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class RoomType(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='images/room_types/',blank=True,null=True)
    max_adult = models.PositiveIntegerField(default=1)
    max_child = models.PositiveIntegerField(default=0)
    max_infant = models.PositiveIntegerField(default=0)
    attributes = models.ManyToManyField(Attribute)
    exposures = models.ManyToManyField(Exposure)
    beds = models.ManyToManyField(BedType, through='RoomTypeBed')
    base_price = models.DecimalField(max_digits=10, decimal_places=2) # Emergency fallback
    def __str__(self):
        return self.name
    
class RoomTypeBed(models.Model):
    """A 'Through' model to store the quantity of each bed type"""
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    bed_type = models.ForeignKey(BedType, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Room(models.Model):
    #Maid Status
    DIRTY = 'DT'
    CLEAN = 'CL'
    CLEANING = 'CG'
    WORKING = 'WG'
    MAID_STATUS = [
        (DIRTY,"Dirty"),
        (CLEAN,"Clean"),
        (CLEANING,"Cleaning"),
        (WORKING,"Working"),
    ]
    no = models.CharField(max_length=255)
    maid_status = models.CharField(max_length=2,choices=MAID_STATUS,default=CLEAN)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='rooms')
    room_type = models.ForeignKey(RoomType,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.no

class AddOnItem(models.Model):
    name = models.CharField(max_length=100) 
    icon_name = models.CharField(max_length=50) # e.g., "bed-icon" (for UI)
    default_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_inventory = models.PositiveIntegerField() 
    category = models.CharField(max_length=50) # e.g., "Bedding", "Food", "Service"

    def get_available_qty(self, date):
        # Logic to subtract items already assigned to other reservations on this date
        pass

    def __str__(self):
        return self.name