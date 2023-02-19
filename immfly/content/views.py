import logging
import traceback

from django.db import IntegrityError
from django.db.models import Q, Prefetch
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics
from rest_framework.response import Response
from .models import Content
from .filters import ContentFilter
from .serializers import ContentSerializer, ListContentSerializer

class ContentView(generics.ListCreateAPIView):
    """
    View for creating contents through the API
    """
    filter_backends = [DjangoFilterBackend, ContentFilter]
    filterset_fields = ['name', 'rating', 'source']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ContentSerializer
        return ListContentSerializer

    def get_queryset(self):
        """
        Content filter for preparing queryset
        """
        name = self.request.query_params.get('name', None)
        rating = self.request.query_params.get('rating', None)
        source = self.request.query_params.get('source', None)
        request = self.request
        condition = Q()
        if name:
            condition = condition & Q(name=name)
        # if provider:
        #     condition = condition & Q(provider__pk=provider)
        # if module:
        #     condition = condition & Q(module=module)
        # if control_class:
        #     condition = condition & Q(control_class=control_class)
        
        return Content.objects.filter(condition)
  
 
    def list(self, request):
        """
        Query for listing contents
        """
        action = 'List Controls'
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            data = {"results": serializer.data}
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            message = e
            service_status = status.HTTP_500_INTERNAL_SERVER_ERROR
            data = {"message" : message}
            return Response(data, status=service_status)