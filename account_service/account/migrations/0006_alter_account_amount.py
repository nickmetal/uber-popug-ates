# Generated by Django 4.0.4 on 2022-05-14 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_account_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
    ]