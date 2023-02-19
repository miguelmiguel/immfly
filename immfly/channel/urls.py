from django.urls import path, re_path

from .views import (ChannelView)

app_name = 'channel'

urlpatterns = [
    # Channel URLS
    path('', ChannelView.as_view(), name='default'),
]