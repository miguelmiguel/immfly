from django.db import IntegrityError
from django.db.models import Q, Prefetch
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics
from rest_framework.response import Response
from .models import Channel
from .filters import ChannelFilter
from .serializers import ChannelSerializer, ListChannelSerializer

class ChannelView(generics.ListCreateAPIView):
    """
    View for creating channels through the API
    """
    filter_backends = [DjangoFilterBackend, ChannelFilter]
    filterset_fields = ['title', 'language', 'picture']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ChannelSerializer
        return ListChannelSerializer

    def get_queryset(self):
        """
        Channel filter for preparing queryset
        """
        title = self.request.query_params.get('title', None)
        language = self.request.query_params.get('language', None)
        request = self.request
        condition = Q()
        if language:
            condition = condition & Q(language=language)
        if title:
            condition = condition & Q(title=title)
        # if module:
        #     condition = condition & Q(module=module)
        # if control_class:
        #     condition = condition & Q(control_class=control_class)
        
        return Channel.objects.filter(condition)
  
 
    def list(self, request):
        """
        Query for listing contents
        """
        action = 'List Channels'
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