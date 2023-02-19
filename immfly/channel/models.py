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

    @property
    def rating(self):
        return self.get_ratings_avg()

    def get_ratings_avg(self):
        channels, contents = {}, {}
        channels, contents = self.channel_rating(channels, contents)
        rating = 0
        index = 0
        for ch in channels.keys():
            rating += channels[ch]
            index += 1
        return rating / index
        
    def channel_rating(self, channels, contents):
        if self.id not in channels:
            channels[self.id] = 0
            index = 0
            rating = 0
            for ct in self.contents.all():
                contents[ct.id] = ct.rating
                rating += ct.rating
                index += 1
            if index > 0:
                channels[self.id] = rating/index
            for ch in self.subchannels.all():
                channels, contents = ch.channel_rating(channels, contents)
        return channels, contents

            

