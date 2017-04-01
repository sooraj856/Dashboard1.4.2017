from __future__ import unicode_literals

from django.db import models

# Create your models here.


class task_item(models.Model):
    task_name = models.CharField(max_length=200)
    task_date = models.DateField(null=True)
    task_time = models.TimeField(null=True)
    task_duration = models.IntegerField()
    task_actual = models.IntegerField()
    task_project = models.CharField(max_length=50)
    task_priority = models.CharField(max_length=50)
    task_status = models.CharField(max_length=50)
    task_category = models.CharField(max_length=50)
    task_note = models.CharField(max_length=500)
    def __unicode__(self):
        return self.task_name
