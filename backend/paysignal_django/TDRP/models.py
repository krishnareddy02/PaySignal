import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Register(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

class transaction_details(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    transaction_id = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    reason = models.CharField(max_length=255)
    details = models.TextField()
    complaint_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='media/',blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'  # Default status is "pending"
    )
