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
        return channels[self.id]
        
    def channel_rating(self, channels, contents):
        if self.id not in channels:
            current_channel = {'rating':0, 'has_contents':False, 'title': self.title}
            index = 0
            rating = 0
            channel_contents = self.contents.all()
            if channel_contents.count() > 0:
                current_channel['has_contents'] = True
                for ct in channel_contents:
                    contents[ct.id] = ct.rating
                    rating += ct.rating
                    index += 1
                if index > 0:
                    current_channel['rating'] = rating/index
                channels[self.id] = current_channel
            else:
                channels[self.id] = current_channel
                for ch in self.subchannels.all():
                    channels, contents = ch.channel_rating(channels, contents)
                    if channels[ch.id]['has_contents']:
                        rating += channels[ch.id]['rating']
                        index += 1
                if index > 0:
                    current_channel['rating'] = rating/index
                channels[self.id] = current_channel
        return channels, contents

    @classmethod
    def get_all_ratings(cls):
        channels = cls.objects.all()
        channels_ratings, contents = {}, {}
        for ch in channels:
            if ch.id not in channels_ratings:
                channels_ratings, contents = ch.channel_rating(channels_ratings, contents)
        return channels_ratings
            

    @classmethod
    def get_all_ratings_sorted(cls, reverse=True):
        ratings = cls.get_all_ratings()
        sorted_channels_by_rating = sorted(ratings.items(), key=lambda x:x[1]['rating'], reverse=reverse)
        return dict(sorted_channels_by_rating)
        