# Generated by Django 4.0.4 on 2022-05-15 09:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_alter_account_public_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='public_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]