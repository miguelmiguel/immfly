from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from common.utils import exception_message
from content.serializers import ContentSerializer
from .models import Channel
from .filters import ChannelFilter
from .serializers import (ChannelSerializer, ListChannelSerializer, 
    ChannelDetailSerializer, ChannelUpdateSerializer)


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


class ChannelDetailView(APIView):
    """
        Details view for a specific Channel in the API
    """
    def get_object(self, id):
        """
        Get details from a specific Channel
        
        Params:
        - id: Channel ID
        """
        condition = Q(pk=id)
        return Channel.objects.prefetch_related('contents').prefetch_related(
            'subchannels').get(condition)

    def get(self, request, id):
        """
        Method that gets the details from a Channel
        
        Params:
        - id: Channel ID
        """
        action = 'Show Channel'
        try:
            channel = self.get_object(id)
            serializer = ChannelDetailSerializer(channel)
            data = {'results': serializer.data}
            return Response(data, status=status.HTTP_200_OK)
        except Channel.DoesNotExist:
            error = f"Channel '{id}' not found"
            service_status = status.HTTP_404_NOT_FOUND
        except Exception as e:
            error = exception_message(e)
            service_status = status.HTTP_500_INTERNAL_SERVER_ERROR

        data = {'message': error}
        return Response(data, status=service_status)
    
    def delete(self, request, id):
        """
        Method that removes a Channel
        
        Params:
        - id: Channel ID to be eliminated
        """
        action = 'Delete Channel'
        try:
            channel = self.get_object(id)
            title = channel.title
            channel.delete()
            data = {'message': f'Channel "{title}" deleted'}
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        except Channel.DoesNotExist:
            error = f"Channel '{id}' not found"
            service_status = status.HTTP_404_NOT_FOUND
        except Exception as e:
            error_me = exception_message(e)
            service_status = status.HTTP_500_INTERNAL_SERVER_ERROR

        data = {'message': error}
        return Response(data, status=service_status)
    
    def put(self, request, id):
        """
        Method that edits a Channel
            
            Params:
            - id: Channel ID to be edited
        """
        action = 'Edit Channel'
        try:
            channel = self.get_object(id)
            serializer = ChannelUpdateSerializer(channel, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                data = {'data': serializer.data}
                return Response(data, status=status.HTTP_200_OK)

            error = "Invalid parameters"
            data = {'data': serializer.errors, 
                'message': error}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        except Channel.DoesNotExist:
            error = f"Channel '{id}' not found"
            service_status = status.HTTP_404_NOT_FOUND
        except Exception as e:
            error = exception_message(e)
            service_status = status.HTTP_500_INTERNAL_SERVER_ERROR

        data = {'message': error}
        return Response(data, status=service_status)


class SubchannelList(APIView):
    def get_queryset(self, id):
        """
        Channel filter for preparing queryset
        """
        return Channel.objects.get(pk=id).subchannels

    def get(self, request, id):
        """
        Method that gets the list of subchannels from a Channel
        
        Params:
        - id: Channel ID
        """
        try:
            queryset = self.get_queryset(id)
            serializer = ChannelSerializer(queryset, many=True)
            return Response(serializer.data)
        except Channel.DoesNotExist:
            error = f"Channel '{id}' not found"
            service_status = status.HTTP_404_NOT_FOUND
        except Exception as e:
            error = exception_message(e)
            service_status = status.HTTP_500_INTERNAL_SERVER_ERROR

        data = {'message': error}
        return Response(data, status=service_status)


class ContentList(APIView):
    def get_queryset(self, id):
        """
        Channel filter for preparing queryset
        """
        return Channel.objects.get(pk=id).contents

    def get(self, request, id):
        """
        Method that gets the list of contents from a Channel
        
        Params:
        - id: Channel ID
        """
        try:
            queryset = self.get_queryset(id)
            serializer = ContentSerializer(queryset, many=True)
            return Response(serializer.data)
        except Channel.DoesNotExist:
            error = f"Channel '{id}' not found"
            service_status = status.HTTP_404_NOT_FOUND
        except Exception as e:
            error = exception_message(e)
            service_status = status.HTTP_500_INTERNAL_SERVER_ERROR

        data = {'message': error}
        return Response(data, status=service_status)