from django.db import models

class Channel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, db_index=True)
    language = models.CharField(max_length=64, db_index=True)
    picture = models.CharField(max_length=512)
    subchannels = models.ManyToManyField('Channel')
    contents = models.ManyToManyField('content.Content')
