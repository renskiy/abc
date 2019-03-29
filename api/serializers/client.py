from rest_framework import serializers

from api.models import Client


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('first_name', 'second_name', 'middle_name')
