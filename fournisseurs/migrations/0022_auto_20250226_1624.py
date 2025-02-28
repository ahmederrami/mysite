# Generated by Django 3.2.25 on 2025-02-26 16:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fournisseurs', '0021_auto_20250226_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiaire',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2025, 2, 26)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='beneficiaire',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.date(2025, 2, 26)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comptetresorerie',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2025, 2, 26)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comptetresorerie',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.date(2025, 2, 26)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contrat',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2025, 2, 26)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contrat',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.date(2025, 2, 26)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='facture',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2025, 2, 26)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='facture',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.date(2025, 2, 26)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ordrevirement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2025, 2, 26)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ordrevirement',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.date(2025, 2, 26)),
            preserve_default=False,
        ),
    ]
