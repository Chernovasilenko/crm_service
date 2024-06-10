from django.contrib.auth import get_user_model
from django.db import models

from crm_django.constants import MAX_LENGHT_CHAR_FIELD, MAX_STR_LENGTH

User = get_user_model()


class Team(models.Model):
    name = models.CharField(max_length=MAX_LENGHT_CHAR_FIELD)
    members = models.ManyToManyField(User, related_name='teams')
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_teams'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name[:MAX_STR_LENGTH]
