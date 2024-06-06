from django.contrib.auth import get_user_model
from rest_framework import viewsets

from client.models import Client
from team.models import Team
from client.serializers import ClientSerializer

User = get_user_model()


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        return self.queryset.filter(team=team)

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        serializer.save(team=team, created_by=self.request.user)
