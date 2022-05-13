# Generated by Django 4.0.4 on 2022-05-13 12:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='public_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
