from django.db import models
from django.core.validators import FileExtensionValidator

class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    diploma = models.FileField(
        upload_to='diplomas/',
        validators=[FileExtensionValidator(['pdf'])],
        blank=True,
        null=True
    )
    image = models.ImageField(upload_to='about/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    live_demo = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/')
    video = models.FileField(
        upload_to='project_videos/',
        validators=[FileExtensionValidator(['mp4', 'webm', 'ogg'])],
        blank=True,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name}"

class Pricing(models.Model):
    SERVICE_TYPES = [
        ('static', 'Static Site'),
        ('business', 'Business Site'),
        ('webapp', 'Web App (Django)'),
        ('shop', 'Web Shop'),
        ('hr', 'HR System (custom)'),
    ]
    
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES, unique=True)
    initial_price = models.DecimalField(max_digits=8, decimal_places=2)
    monthly_maintenance = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    features = models.TextField(help_text="List features separated by new lines")

    def __str__(self):
        return self.get_service_type_display()