# Generated by Django 3.2.25 on 2025-03-13 15:42

from django.db import migrations, models
import operationsDiverses.models


class Migration(migrations.Migration):

    dependencies = [
        ('operationsDiverses', '0002_auto_20250312_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='operationdiverse',
            name='annee_comptable',
            field=models.IntegerField(default=2025, validators=[operationsDiverses.models.validate_annee]),
        ),
    ]
