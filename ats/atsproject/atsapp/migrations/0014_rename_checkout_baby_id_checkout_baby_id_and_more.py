# Generated by Django 5.0.3 on 2024-06-05 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atsapp', '0013_rename_baby_id_checkout_checkout_baby_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkout',
            old_name='checkout_baby_id',
            new_name='baby_id',
        ),
        migrations.RenameField(
            model_name='checkout',
            old_name='checkout_sitter_id',
            new_name='sitter_id',
        ),
    ]
