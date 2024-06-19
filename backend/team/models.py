from django.contrib.auth import get_user_model
from django.db import models

from crm_django import constants as const

User = get_user_model()


class Plan(models.Model):
    name = models.CharField(max_length=const.MAX_LENGHT_CHAR_FIELD)
    max_leads = models.IntegerField(default=const.DEFAULT_LEADS_IN_PLAN)
    max_clients = models.IntegerField(default=const.DEFAULT_CLIENTS_IN_PLAN)
    price = models.IntegerField(default=const.DEFAULT_PRICE)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=const.MAX_LENGHT_CHAR_FIELD)
    members = models.ManyToManyField(User, related_name='teams')
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_teams'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    plan = models.ForeignKey(
        Plan,
        on_delete=models.SET_NULL,
        related_name='teams',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name[:const.MAX_STR_LENGTH]
