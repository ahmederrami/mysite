# Generated by Django 3.2.25 on 2025-02-19 12:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fournisseurs', '0010_ordrevirement_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiaire',
            name='adresse',
            field=models.CharField(blank=True, help_text='Adresse du bénéficiaire', max_length=50, null=True, verbose_name='Adresse'),
        ),
        migrations.AddField(
            model_name='beneficiaire',
            name='telephone',
            field=models.CharField(blank=True, error_messages={'unique': 'Ce numéro de téléphone est déjà utilisé.'}, help_text='Numéro de téléphone', max_length=10, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='Le numéro de téléphone doit contenir exactement 10 chiffres.', regex='^\\d{10}$')], verbose_name='Téléphone'),
        ),
        migrations.AddField(
            model_name='beneficiaire',
            name='ville',
            field=models.CharField(blank=True, help_text='Ville', max_length=20, null=True, verbose_name='Ville'),
        ),
        migrations.AlterField(
            model_name='ordrevirement',
            name='reference',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name="Autre référence de l'ordre de virement si édité sur un autre système"),
        ),
    ]
