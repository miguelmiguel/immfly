from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from ..models import Channel
from content.models import Content

# initialize the APIClient app
client = Client()

def set_up_user(instance):
    instance.user, created = User.objects.get_or_create(is_superuser=True, 
        username="MyUsername")
    instance.user.set_password("My-Password")
    instance.user.save()

    logged_in = client.login(username='MyUsername', password='My-Password')

def set_up_contents(instance):
    instance.content_1 = Content.objects.create(pk=1, name="Content 1", rating=20, 
        source="content1.pdf", metadata={'languages':['english', 'spanish'], 
        'description':{'spanish': 'Primer contenido', 'english': 'First content'}})
    instance.content_2 = Content.objects.create(pk=2, name="Content 2", rating=100, 
        source="content2.mp4", metadata={'languages':['english', 'spanish'], 
        'description':{'spanish': 'Segundo contenido', 'english': 'Second content'}})
    instance.content_3 = Content.objects.create(pk=3, name="Content 3", rating=10, 
        source="content3.txt", metadata={'languages':['english', 'spanish'], 
        'description':{'spanish': 'Tercer contenido', 'english': 'Tercer content'}})
    instance.content_4 = Content.objects.create(pk=4, name="Content 4", rating=30, 
        source="content4.txt", metadata={'languages':['english', 'spanish'], 
        'description':{'spanish': 'Cuarto contenido', 'english': 'Fourth content'}})
    instance.content_5 = Content.objects.create(pk=5, name="Content 5", rating=80, 
        source="content5.mp4", metadata={'languages':['english', 'spanish'], 
        'description':{'spanish': 'Quinto contenido', 'english': 'Fifth content'}})

def set_up_channels(instance):
    instance.channel_1 = Channel.objects.create(
        title='Test Channel 1', language="Spanish", 
        picture='path_to_picture_for_channel_1.png',
    )
    instance.channel_1.contents.set([instance.content_1, instance.content_2])
    
    instance.channel_2 = Channel.objects.create(
        title='Test Channel 2', language="Spanish", 
        picture='path_to_picture_for_channel_2.png', 
    )
    instance.channel_2.contents.set([instance.content_1, instance.content_2])

    instance.channel_3 = Channel.objects.create(
        title='Test Channel 3', language="Spanish", 
        picture='path_to_picture_for_channel_3.png',
    )
    instance.channel_3.subchannels.set([instance.channel_1])

    instance.channel_4 = Channel.objects.create(
        title='Test Channel 4', language="Spanish", 
        picture='path_to_picture_for_channel_4.png', 
    )
    instance.channel_4.subchannels.set([instance.channel_2, instance.channel_3])

    instance.channel_5 = Channel.objects.create(
        title='Test Channel 5', language="Spanish", 
        picture='path_to_picture_for_channel_5.png', 
    )
    instance.channel_5.subchannels.set([instance.channel_2])

    instance.channel_6 = Channel.objects.create(
        title='Test Channel 6', language="Spanish", 
        picture='path_to_picture_for_channel_6.png', 
    )
    instance.channel_6.contents.set([instance.content_3])

class GetRatingsTest(TestCase):
    """ Test module for ratings algorithm """

    def setUp(self):
        set_up_user(self)
        set_up_contents(self)
        set_up_channels(self)

    def test_get_channel_rating(self):
        rating_6 = self.channel_6.rating['rating']
        self.assertEqual(rating_6, 10)
        rating_got = self.channel_6.get_ra
        rating_1 = self.channel_1.rating['rating']
        # content_1 rating = 20
        # content_2 rating = 100
        # avg = 60
        self.assertNotEqual(rating_1, 10)
        self.assertEqual(rating_1, 60)