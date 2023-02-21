from django.urls import path, re_path

from .views import (ChannelView, ChannelDetailView, SubchannelList, ContentList)

app_name = 'channel'

urlpatterns = [
    # Channel URLS
    path('', ChannelView.as_view(), name='default'),
    path('<int:id>', ChannelDetailView.as_view(), name='detail'),
    path('<int:id>/subchannels', SubchannelList.as_view(), name='subchannels'),
    path('<int:id>/contents', ContentList.as_view(), name='contents'),
]