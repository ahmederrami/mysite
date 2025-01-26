# Generated by Django 3.2.25 on 2024-05-30 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stages', '0006_stage_traite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='selectedPeriode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stages', to='stages.periode'),
        ),
    ]
