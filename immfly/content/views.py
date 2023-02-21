from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from common.utils import exception_message
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
        
        return Content.objects.filter(condition)
  
 
    def list(self, request):
        """
        Query for listing contents
        """
        action = 'List Contents'
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


class ContentDetailView(APIView):
    """
        Details view for a specific Content in the API
    """
    def get_object(self, id):
        """
        Get details from a specific Content
        
        Params:
        - id: Channel ID
        """
        condition = Q(pk=id)
        return Content.objects.get(condition)

    def get(self, request, id):
        """
        Method that gets the details from a Content
        
        Params:
        - id: Content ID
        """
        action = 'Show Content'
        try:
            content = self.get_object(id)
            serializer = ListContentSerializer(content)
            data = {'results': serializer.data}
            return Response(data, status=status.HTTP_200_OK)
        except Content.DoesNotExist:
            error = f"Content '{id}' not found"
            service_status = status.HTTP_404_NOT_FOUND
        except Exception as e:
            error = exception_message(e)
            service_status = status.HTTP_500_INTERNAL_SERVER_ERROR

        data = {'message': error}
        return Response(data, status=service_status)
    
    def delete(self, request, id):
        """
        Method that removes a Content
        
        Params:
        - id: Content ID to be eliminated
        """
        action = 'Delete Content'
        try:
            content = self.get_object(id)
            name = content.name
            content.delete()
            data = {'message': f'Content "{name}" deleted'}
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        except Content.DoesNotExist:
            error = f"Content '{id}' not found"
            service_status = status.HTTP_404_NOT_FOUND
        except Exception as e:
            error_me = exception_message(e)
            service_status = status.HTTP_500_INTERNAL_SERVER_ERROR

        data = {'message': error}
        return Response(data, status=service_status)
    
    def put(self, request, id):
        """
        Method that edits a Content
            
            Params:
            - id: Content ID to be edited
        """
        action = 'Edit Content'
        try:
            content = self.get_object(id)
            serializer = ContentSerializer(content, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                data = {'data': serializer.data}
                return Response(data, status=status.HTTP_200_OK)

            error = "Invalid parameters"
            data = {'data': serializer.errors, 
                'message': error}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        except Content.DoesNotExist:
            error = f"Content '{id}' not found"
            service_status = status.HTTP_404_NOT_FOUND
        except Exception as e:
            error = exception_message(e)
            service_status = status.HTTP_500_INTERNAL_SERVER_ERROR

        data = {'message': error}
        return Response(data, status=service_status)