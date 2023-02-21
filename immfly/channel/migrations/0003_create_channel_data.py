from django.db import migrations

def forwards(apps, schema_editor):
    # Creation of Channels for the app
    Content = apps.get_model('content', 'Content')
    content_1 = Content.objects.get_or_create(name="Content 1", rating=20, 
        source="content1.pdf", metadata={'languages':['english', 'spanish'], 
        'description':{'spanish': 'Primer contenido', 'english': 'First content'}})
    content_2 = Content.objects.get_or_create(name="Content 2", rating=100, 
        source="content2.mp4", metadata={'languages':['english', 'spanish'], 
        'description':{'spanish': 'Segundo contenido', 'english': 'Second content'}})
    content_3 = Content.objects.get_or_create(name="Content 3", rating=10, 
        source="content3.txt", metadata={'languages':['english', 'spanish'], 
        'description':{'spanish': 'Tercer contenido', 'english': 'Third content'}})
    content_4 = Content.objects.get_or_create(name="Content 4", rating=30, 
        source="content4.txt", metadata={'languages':['english', 'spanish'], 
        'description':{'spanish': 'Cuarto contenido', 'english': 'Fourth content'}})
    content_5 = Content.objects.get_or_create(name="Content 5", rating=80, 
        source="content5.mp4", metadata={'languages':['english', 'spanish'], 
        'description':{'spanish': 'Quinto contenido', 'english': 'Fifth content'}})
    if content_1 and content_1[0]:
        content_1 = content_1[0]
    if content_2 and content_2[0]:
        content_2 = content_2[0]
    if content_3 and content_3[0]:
        content_3 = content_3[0]
    if content_4 and content_4[0]:
        content_4 = content_4[0]
    if content_5 and content_5[0]:
        content_5 = content_5[0]


    Channel = apps.get_model('channel', 'Channel')
    channel_1 = Channel.objects.create(
        title='My Channel 1', language="Spanish", 
        picture='path_to_picture_for_channel_1.png',
    )
    channel_1.contents.set([content_1, content_2])
    
    channel_2 = Channel.objects.create(
        title='My Channel 2', language="Spanish", 
        picture='path_to_picture_for_channel_2.png', 
    )
    channel_2.contents.set([content_1, content_2])

    channel_3 = Channel.objects.create(
        title='My Channel 3', language="Spanish", 
        picture='path_to_picture_for_channel_3.png',
    )
    channel_3.subchannels.set([channel_1])

    channel_4 = Channel.objects.create(
        title='My Channel 4', language="Spanish", 
        picture='path_to_picture_for_channel_4.png', 
    )
    channel_4.subchannels.set([channel_2, channel_3])

    channel_5 = Channel.objects.create(
        title='My Channel 5', language="Spanish", 
        picture='path_to_picture_for_channel_5.png', 
    )
    channel_5.subchannels.set([channel_2])

    channel_6 = Channel.objects.create(
        title='My Channel 6', language="Spanish", 
        picture='path_to_picture_for_channel_6.png', 
    )
    channel_6.contents.set([content_3])


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0002_alter_channel_contents_alter_channel_subchannels'),
        ('content', '0003_create_content_data'),
    ]

    operations = [
        migrations.RunPython(forwards),
    ]