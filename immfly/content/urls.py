from django.urls import path, re_path

from .views import (ContentView)

app_name = 'content'

urlpatterns = [
    # Content URLS
    path('', ContentView.as_view(), name='default'),
]