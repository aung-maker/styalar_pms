from django.db import models

# Create your models here.
class Gender(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255)
    flag = models.CharField(max_length=255, null=True, blank=True) 
    iso_code = models.CharField(max_length=2, unique=True)
    def __str__(self):
        return self.name
    


class Guest(models.Model):
      ID = "I"
      PASSPORT = "P"
      IDENTITY_TYPE = [
          (ID,"ID Card"),
          (PASSPORT, "Passport")
      ]
      gender = models.CharField(max_length=255)
      name = models.CharField(max_length=255)
      profile = models.ImageField(upload_to="images/guests/",null=True,blank=True)
      is_owner = models.BooleanField(default=False)
      is_vip = models.BooleanField(default=False)
      owner_name = models.CharField(max_length=255,null=True,blank=True)
      address = models.TextField(null=True,blank=True)
      country = models.CharField(max_length=255,null=True,blank=True)
      state = models.CharField(max_length=255,null=True,blank=True)
      city = models.CharField(max_length=255,null=True,blank=True)
      zip_code = models.CharField(max_length=255,null=True,blank=True)
      mobile_code = models.CharField(max_length=255,null=True,blank=True)
      mobile_no = models.CharField(max_length=255,null=True,blank=True)
      tele_code = models.CharField(max_length=255,null=True,blank=True)
      tele_no = models.CharField(max_length=255,null=True,blank=True)
      email = models.CharField(max_length=255,null=True,blank=True)
      identity_type = models.CharField(max_length=1,choices=IDENTITY_TYPE,default=PASSPORT)
      nationality = models.CharField(max_length=255,null=True,blank=True)
      country = models.ForeignKey(
        Country, 
        on_delete=models.PROTECT, 
        related_name='guests',
        null=True,
        blank=True
    )
      id_card = models.CharField(max_length=255,null=True,blank=True)
      passport_number = models.CharField(max_length=255,null=True,blank=True)
      local_name = models.CharField(max_length=255,null=True,blank=True)
      date_of_birth = models.DateField(null=True, blank=True)
      issue_date = models.DateField(null=True, blank=True)
      expire_date = models.DateField(null=True, blank=True)
      is_primary = models.BooleanField(default=False)



class Organization(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    market_segment = models.ForeignKey('finance.MarketSegment', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class ARAccount(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
