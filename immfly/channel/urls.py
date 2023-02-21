from django.urls import path, re_path

from .views import (ChannelView, ChannelDetailView)

app_name = 'channel'

urlpatterns = [
    # Channel URLS
    path('', ChannelView.as_view(), name='default'),
    path('<int:id>', ChannelDetailView.as_view(), name='detail'),
]