# Generated by Django 3.2.25 on 2024-05-26 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stages', '0004_alter_stage_specialite'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='commentaire',
            field=models.TextField(blank=True, null=True),
        ),
    ]
