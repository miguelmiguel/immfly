from rest_framework import serializers

from .models import Channel

class ChannelSerializer(serializers.ModelSerializer):
  class Meta:
    model = Channel
    fields = ['id', 'title', 'language', 'picture', 'subchannels', 'contents']
    read_only_fields = ['id']

  def validate(self, data):
    subchannels = data.get('subchannels', [])
    contents = data.get('contents', [])
    subchannel_size = len(subchannels)
    content_size = len(contents)
    if subchannel_size == 0 and content_size == 0:
      raise serializers.ValidationError("A Channel must have at least "\
        "one subchannel or one content related")
    elif subchannel_size > 0 and content_size > 0:
      raise serializers.ValidationError("A Channel must have only "\
        "subchannels or only contents related")
    return data

class ListChannelSerializer(serializers.ModelSerializer):
  class Meta:
    model = Channel
    fields = ['id', 'title', 'language', 'picture', 'subchannels', 'contents']
    read_only_fields = ['id', 'title', 'language', 'picture', 'subchannels', 'contents']


class ChannelDetailSerializer(serializers.ModelSerializer):
  """
    Channel details serializer
  """
  rating = serializers.ReadOnlyField()
  # framework_set = FrameworkReadSerializer(many=True, read_only=True)

  class Meta:
    model = Channel
    fields = ['id', 'title', 'language', 'picture', 'subchannels', 'contents',
      'rating']
    read_only_fields = ['id', 'title', 'language', 'picture', 'subchannels', 
      'contents', 'rating']


class ChannelUpdateSerializer(serializers.ModelSerializer):
  """
    Update Channel Serializer
  """
  class Meta:
    model = Channel
    fields = ['id', 'title', 'language', 'picture', 'subchannels', 'contents']
    read_only_fields = ['id']

  def validate(self, data):
    subchannels = data.get('subchannels', [])
    contents = data.get('contents', [])
    subchannel_size = len(subchannels)
    content_size = len(contents)
    if subchannel_size == 0 and content_size == 0:
      raise serializers.ValidationError("A Channel must have at least "\
        "one subchannel or one content related")
    elif subchannel_size > 0 and content_size > 0:
      raise serializers.ValidationError("A Channel must have only "\
        "subchannels or only contents related")
    return data