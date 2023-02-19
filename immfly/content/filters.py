import coreapi
from rest_framework import filters


class ContentFilter(filters.BaseFilterBackend):
  def filter_queryset(self, request, queryset, view):
    return queryset

  def get_schema_fields(self, view):
    fields = [
      coreapi.Field(name="name", description="Name", required=False, location='query'),
      coreapi.Field(name="source", description="Source", required=False, location='query'),
      coreapi.Field(name="rating", description="Rating", required=False, location='query'),
    ]

    return fields