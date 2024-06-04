from rest_framework import viewsets

from .models import Lead
from .serializers import LeadSerializer


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        return super().perform_create(serializer)
