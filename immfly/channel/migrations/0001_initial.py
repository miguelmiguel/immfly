# Generated by Django 4.1.7 on 2023-02-19 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(db_index=True, max_length=64)),
                ('language', models.CharField(db_index=True, max_length=64)),
                ('picture', models.CharField(max_length=512)),
                ('contents', models.ManyToManyField(to='content.content')),
                ('subchannels', models.ManyToManyField(to='channel.channel')),
            ],
        ),
    ]
