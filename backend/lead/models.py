from django.contrib.auth import get_user_model
from django.db import models

from crm_django.constants import (
    MAX_LENGHT_CHAR_FIELD, MAX_LENGHT_PHONE_FIELD, MAX_STR_LENGTH
)
from team.models import Team

User = get_user_model()


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

    team = models.ForeignKey(
        Team,
        related_name='leads',
        on_delete=models.CASCADE
    )
    company = models.CharField(max_length=MAX_LENGHT_CHAR_FIELD)
    contact_name = models.CharField(max_length=MAX_LENGHT_CHAR_FIELD)
    email = models.EmailField()
    phone = models.CharField(max_length=MAX_LENGHT_PHONE_FIELD)
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
    assigned_to = models.ForeignKey(
        User,
        blank=True,
        null=True,
        related_name='assigned_leads',
        on_delete=models.SET_NULL
    )
    created_by = models.ForeignKey(
        User,
        related_name='leads',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company[:MAX_STR_LENGTH]
