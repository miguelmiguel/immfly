from django.db import models
from django.forms import ValidationError

class Channel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, db_index=True)
    language = models.CharField(max_length=64, db_index=True)
    picture = models.CharField(max_length=512)
    subchannels = models.ManyToManyField('Channel', blank=True)
    contents = models.ManyToManyField('content.Content', blank=True)

    # def clean(self) -> None:
    #     return super().clean()
    # def save(self, *args, **kwargs):
    #     if self.contents.acount() > 0 and self.subchannels.count() > 0:
    #         raise ValidationError('Channels cannot contain contents and subchannels')
    #     super(Channel, self).save(*args, **kwargs)

        