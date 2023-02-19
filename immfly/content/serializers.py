from rest_framework import serializers

from .models import Content


class ContentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Content
    fields = ['id', 'name', 'rating', 'source', 'metadata']
    read_only_fields = ['id']

class ListContentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Content
    fields = ['id', 'name', 'rating', 'source', 'metadata']
    read_only_fields = ['id', 'name', 'rating', 'source', 'metadata']
