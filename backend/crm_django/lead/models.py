from django.contrib.auth.models import User
from django.db import models


class Lead(models.Model):

    NEW = 'new'
    CONTACTED = 'contacted'
    IN_PROGRESS = 'in_progress'
    WON = 'won'
    LOST = 'lost'

    STATUS_CHOICES = (
        (NEW, 'New'),
        (CONTACTED, 'Contacted'),
        (IN_PROGRESS, 'In Progress'),
        (WON, 'Won'),
        (LOST, 'Lost'),
    )

    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    PRIORITY_CHOICES = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )

    company = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    website = models.URLField(blank=True, null=True)
    confidence = models.IntegerField(blank=True, null=True)
    estimated_value = models.IntegerField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=NEW
    )
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default=MEDIUM
    )
    created_by = models.ForeignKey(
        User, related_name='leads', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company
