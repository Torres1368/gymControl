# Generated by Django 5.0.7 on 2025-04-19 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymcontrol', '0005_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='abono',
            old_name='Suscripcion',
            new_name='suscripcion',
        ),
    ]
