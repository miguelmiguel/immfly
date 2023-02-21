from django.db import migrations

def forwards(apps, schema_editor):
    # Creation of Contents for the app
    Content = apps.get_model('content', 'Content')
    Content.objects.get_or_create(name="Content 1", rating=20, 
        source="content1.pdf", metadata={'languages':['english', 'spanish'], 
        'description':{'spanish': 'Primer contenido', 'english': 'First content'}})
    Content.objects.get_or_create(name="Content 2", rating=100, 
        source="content2.mp4", metadata={'languages':['english', 'spanish'], 
        'description':{'spanish': 'Segundo contenido', 'english': 'Second content'}})
    Content.objects.get_or_create(name="Content 3", rating=10, 
        source="content3.txt", metadata={'languages':['english', 'spanish'], 
        'description':{'spanish': 'Tercer contenido', 'english': 'Third content'}})
    Content.objects.get_or_create(name="Content 4", rating=30, 
        source="content4.txt", metadata={'languages':['english', 'spanish'], 
        'description':{'spanish': 'Cuarto contenido', 'english': 'Fourth content'}})
    Content.objects.get_or_create(name="Content 5", rating=80, 
        source="content5.mp4", metadata={'languages':['english', 'spanish'], 
        'description':{'spanish': 'Quinto contenido', 'english': 'Fifth content'}})


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_alter_content_name'),
    ]

    operations = [
        migrations.RunPython(forwards),
    ]