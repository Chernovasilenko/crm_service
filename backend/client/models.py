from django.contrib.auth import get_user_model
from django.db import models

from team.models import Team

User = get_user_model()


class Client(models.Model):

    team = models.ForeignKey(
        Team,
        related_name='clients',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    website = models.URLField(blank=True, null=True)
    created_by = models.ForeignKey(
        User,
        related_name='clients',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
