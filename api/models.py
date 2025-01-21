from django.db import models



class Request(models.Model):
    title = models.CharField(max_length=32)
    fullName = models.CharField(max_length=32)
    address = models.CharField(max_length=64)
    phoneNumber = models.CharField(max_length=12)
    
    militaryChoices = (
        ('accompli', 'مؤدي'),
        ('sursitaire', 'مؤجل'),
        ('exempté', 'معفى')
    )
    driverChoices = (
        ('A', 'صنف A'),
        ('B', 'صنف B'),
        ('C', 'صنف C')
    )
    military = models.CharField(max_length=12, choices=militaryChoices, blank=True)
    driver = models.CharField(max_length=8, choices=driverChoices, blank=True)
    receiver = models.CharField(max_length=32)
    subject = models.CharField(max_length=64)
    body = models.CharField(max_length=1024)
    