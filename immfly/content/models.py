from django.db import models
from django.utils.translation import gettext as _


class Content(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, db_index=True)
    rating = models.DecimalField(decimal_places=2, max_digits=5, db_index=True)
    source = models.CharField(max_length=512)
    metadata = models.JSONField(null=True)


# class ContentMetaData(models.Model):
#     id = models.CharField(primary_key=True, max_length=64)
#     content = models.ForeignKey('Content', on_delete=models.CASCADE, related_name='metadata')
#     data_type = models.CharField(max_length=256, db_index=True)
#     data = models.JSONField(null=True)