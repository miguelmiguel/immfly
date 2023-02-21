from django.urls import path, re_path

from .views import (ContentView, ContentDetailView)

app_name = 'content'

urlpatterns = [
    # Content URLS
    path('', ContentView.as_view(), name='default'),
    path('<int:id>', ContentDetailView.as_view(), name='detail'),
]