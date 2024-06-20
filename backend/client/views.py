from django.contrib.auth import get_user_model
from rest_framework import filters, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from client.models import Client, Note
from client.serializers import ClientSerializer, NoteSerializer
from crm_django import constants as const
from lead.models import Lead
from team.models import Team

User = get_user_model()


class ClientPagination(PageNumberPagination):
    page_size = const.PAGE_SAZE


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = ClientPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'contact_name')

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        return self.queryset.filter(team=team)

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        serializer.save(team=team, created_by=self.request.user)


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        client_id = self.request.GET.get('client_id')
        return self.queryset.filter(team=team).filter(client_id=client_id)

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        client_id = self.request.data.get('client_id')
        serializer.save(
            team=team, created_by=self.request.user, client_id=client_id
        )


@api_view(['POST'])
def convert_lead_to_client(request):
    team = Team.objects.filter(members__in=[request.user]).first()
    lead_id = request.data['lead_id']

    try:
        lead = Lead.objects.get(id=lead_id)
    except Lead.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    Client.objects.create(
        team=team,
        name=lead.company,
        contact_name=lead.contact_name,
        email=lead.email,
        phone=lead.phone,
        website=lead.website,
        created_by=request.user,
    )

    return Response(status=status.HTTP_201_CREATED)
