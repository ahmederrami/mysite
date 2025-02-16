# Generated by Django 3.2.25 on 2025-02-13 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fournisseurs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordrevirement',
            old_name='valide_pour_paiement',
            new_name='remis_a_banque',
        ),
        migrations.RemoveField(
            model_name='ordrevirement',
            name='OV_signe_pdf',
        ),
        migrations.AddField(
            model_name='facture',
            name='proforma_pdf',
            field=models.FileField(blank=True, help_text='Fichier PDF de la facture proforma', null=True, upload_to='proformas/', verbose_name='Proforma PDF'),
        ),
        migrations.AddField(
            model_name='facture',
            name='statut',
            field=models.CharField(choices=[('attente', 'En attente'), ('etablissement', "OV en cours d'établissement"), ('signature', 'OV en cours de signature'), ('banque', 'OV remis à la banque')], default='attente', max_length=30, verbose_name='Statut de la facture'),
        ),
        migrations.AddField(
            model_name='ordrevirement',
            name='OV_remis_banque_pdf',
            field=models.FileField(blank=True, help_text="Fichier PDF de l'OV avec AR banque", null=True, upload_to='virements/', verbose_name='OV signe PDF'),
        ),
    ]
