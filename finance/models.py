from django.db import models

class MarketSegment(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
# Create your models here.
class RatePlan(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    market_segment = models.ForeignKey(MarketSegment, on_delete=models.CASCADE)
    organization = models.ForeignKey(
        'crm.Organization', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    def __str__(self):
        return self.name

class RoomRate(models.Model):
    rate_plan = models.ForeignKey(RatePlan, on_delete=models.CASCADE, related_name='rates')
    room_type = models.ForeignKey('inventory.RoomType', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        # Prevent overlapping rates for the same plan/room type
        ordering = ['start_date']

    def __str__(self):
        return f"{self.rate_plan.code} | {self.room_type.name} | {self.price}"