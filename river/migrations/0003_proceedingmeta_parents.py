# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from river.models.factories import ProceedingMetaObjectFactory
from river.services.proceeding_meta import ProceedingMetaService


class Migration(migrations.Migration):
    dependencies = [
        ('river', '0002_auto_20150916_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='proceedingmeta',
            name='parents',
            field=models.ManyToManyField(related_name='children', verbose_name=b'parents', to='river.ProceedingMeta', db_index=True),
        )
    ]