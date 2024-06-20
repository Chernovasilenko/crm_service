from django.contrib.auth import get_user_model
from rest_framework import filters, viewsets
from rest_framework.pagination import PageNumberPagination

from crm_django import constants as const
from lead.models import Lead
from team.models import Team
from lead.serializers import LeadSerializer

User = get_user_model()


class LeadPagination(PageNumberPagination):
    page_size = const.PAGE_SAZE


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    pagination_class = LeadPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('company', 'contact_name')

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        return self.queryset.filter(team=team)

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        serializer.save(team=team, created_by=self.request.user)

    def perform_update(self, serializer):
        # obj = self.get_object()
        member_id = self.request.data['assigned_to']
        if member_id:
            user = User.objects.get(id=member_id)
            serializer.save(assigned_to=user)
        else:
            serializer.save()
