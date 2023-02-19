import coreapi
from rest_framework import filters


class ChannelFilter(filters.BaseFilterBackend):
  def filter_queryset(self, request, queryset, view):
    return queryset

  def get_schema_fields(self, view):
    fields = [
      coreapi.Field(name="title", description="Title", required=False, location='query'),
      coreapi.Field(name="language", description="Language", required=False, location='query'),
      coreapi.Field(name="picture", description="Picture", required=False, location='query'),
      coreapi.Field(name="subchannels", description="Subchannels", required=False, location='query'),
      coreapi.Field(name="contents", description="Contents", required=False, location='query'),
    ]

    return fields