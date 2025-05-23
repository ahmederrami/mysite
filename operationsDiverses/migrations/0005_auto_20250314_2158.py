# Generated by Django 3.2.25 on 2025-03-14 21:58

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operationsDiverses', '0004_operationdiverse_valide'),
    ]

    operations = [
        migrations.AddField(
            model_name='operationdiverse',
            name='total_credit',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=15),
        ),
        migrations.AddField(
            model_name='operationdiverse',
            name='total_debit',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=15),
        ),
    ]
