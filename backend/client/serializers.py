from rest_framework import serializers

from client.models import Client


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        read_only_fields = ('created_by', 'created_at', 'modified_at')
        fields = (
            'id',
            'name',
            'contact_name',
            'email',
            'phone',
            'website',
            'created_at',
            'modified_at'
        )
