# Generated by Django 3.2.25 on 2025-03-31 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fournisseurs', '0032_alter_avoir_facture_associee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contrat',
            old_name='contrat_actif',
            new_name='actif',
        ),
        migrations.AddField(
            model_name='beneficiaire',
            name='actif',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comptetresorerie',
            name='actif',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='avoir',
            name='facture_associee',
            field=models.ForeignKey(limit_choices_to={'statut': 'attente'}, on_delete=django.db.models.deletion.CASCADE, related_name='facture_avoirs', to='fournisseurs.facture', verbose_name='Facture associée'),
        ),
        migrations.AlterField(
            model_name='comptetresorerie',
            name='beneficiaire',
            field=models.ForeignKey(limit_choices_to={'actif': True}, on_delete=django.db.models.deletion.CASCADE, related_name='comptes', to='fournisseurs.beneficiaire', verbose_name='Bénéficiaire'),
        ),
        migrations.AlterField(
            model_name='contrat',
            name='beneficiaire',
            field=models.ForeignKey(limit_choices_to={'actif': True}, on_delete=django.db.models.deletion.PROTECT, related_name='contrats', to='fournisseurs.beneficiaire', verbose_name='Bénéficiaire'),
        ),
        migrations.AlterField(
            model_name='facture',
            name='beneficiaire',
            field=models.ForeignKey(limit_choices_to={'actif': True}, on_delete=django.db.models.deletion.CASCADE, related_name='factures_beneficiaire', to='fournisseurs.beneficiaire', verbose_name='Bénéficiaire'),
        ),
    ]
