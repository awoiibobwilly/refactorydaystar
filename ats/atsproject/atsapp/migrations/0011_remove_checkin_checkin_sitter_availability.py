# Generated by Django 5.0.3 on 2024-06-03 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atsapp', '0010_alter_checkin_daystar_checkin_fee_currency_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkin',
            name='checkin_sitter_availability',
        ),
    ]
