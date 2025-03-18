# Generated by Django 3.2.25 on 2025-03-12 12:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operationsDiverses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ecritureoperation',
            old_name='type_operation',
            new_name='sens_ecriture',
        ),
        migrations.AddField(
            model_name='operationdiverse',
            name='justif_pdf',
            field=models.FileField(blank=True, help_text="Justifications de l'opération", null=True, upload_to='operationsDiverses/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='Justifications'),
        ),
    ]
