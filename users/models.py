from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('admin', 'General Manager'),
        ('frontdesk', 'Front Office Staff'),
        ('finance', 'Accountant'),
    )

    email = models.EmailField(unique=True) 
    first_name = models.CharField(max_length=150) 
    last_name = models.CharField(max_length=150)  
    mobile_number = models.CharField(max_length=20, blank=True) 
    address = models.TextField(blank=True) 

    # PMS Specific Fields
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='frontdesk')
    department = models.CharField(max_length=100, blank=True)
    
    # Django Permissions
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) 

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    @property
    def username(self):
        """
        JET looks for 'username'. We return 'email' so the 
        template doesn't crash.
        """
        return self.email

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
    
