from django.db import models
from django.conf import settings

# Create your models here.
class Source(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Reservation(models.Model):
    RESERVATION_TYPE = (
        ('reserved', 'Reserved'),
        ('checked-in', 'Checked-In'),
        ('in-house', 'In-House'),
        ('checked-out', 'Checked-Out'),
        ('cancelled', 'Cancelled'),
    )

    arrival_date = models.DateTimeField()
    departure_date = models.DateTimeField()
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    adults = models.PositiveIntegerField(default=1)
    children = models.PositiveIntegerField(default=0)
    
    market_segment = models.ForeignKey('finance.MarketSegment', on_delete=models.PROTECT)
    source = models.ForeignKey(Source, on_delete=models.PROTECT)
    organization = models.ForeignKey('crm.Organization', on_delete=models.SET_NULL, null=True, blank=True)

    room = models.ForeignKey('inventory.Room', on_delete=models.SET_NULL, null=True, blank=True)
    room_type = models.ForeignKey('inventory.RoomType', on_delete=models.PROTECT)
    rate_plan = models.ForeignKey('finance.RatePlan', on_delete=models.PROTECT)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2) 
    
    guests = models.ManyToManyField(
        'crm.Guest', 
        through='ReservationGuest',
        related_name='reservations'
    )
    primary_guest = models.ForeignKey(
        'crm.Guest',
        on_delete=models.PROTECT,
        related_name='primary_reservations',
        null=True
    )
    
    reservation_number = models.CharField(max_length=20, unique=True)
    reservation_type = models.CharField(max_length=20, choices=RESERVATION_TYPE, default='reserved')    
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='reservations_created'
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='reservations_updated'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Res: {self.reservation_number} - {self.primary_guest.name if self.primary_guest else 'No Guest'}"
    

class ReservationGuest(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    guest = models.ForeignKey('crm.Guest', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('reservation', 'guest')

class ReservationRequest(models.Model):
    POSTING_CHOICES = [
        ('EACH_DAY', 'Each Day'),
        ('ONCE', 'Once'),
    ]
    FOLIO_CHOICES = [
        ('GUEST', 'Guest'),
        ('ORG', 'Organization'),
    ]

    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='requests')
    item = models.ForeignKey('inventory.AddOnItem', on_delete=models.PROTECT)
    
    unit_price = models.DecimalField(max_digits=10, decimal_places=2) 
    quantity = models.PositiveIntegerField(default=1)
    
    # Schedule logic
    date_range_start = models.DateField()
    date_range_end = models.DateField()
    posting_schedule = models.CharField(max_length=20, choices=POSTING_CHOICES)
    
    # Billing logic
    folio_target = models.CharField(max_length=20, choices=FOLIO_CHOICES)
    include_in_package = models.BooleanField(default=False)

    @property
    def total_amount(self):
        return self.unit_price * self.quantity