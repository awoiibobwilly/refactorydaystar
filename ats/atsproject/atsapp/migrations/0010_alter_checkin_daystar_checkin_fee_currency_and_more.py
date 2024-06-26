# Generated by Django 5.0.3 on 2024-05-19 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atsapp', '0009_alter_sales_so_item_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='daystar_checkin_fee_currency',
            field=models.CharField(choices=[('UGX', 'UGX'), ('USD', 'USD')], default='UGX', max_length=10),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='daystar_care_time_fee_currency',
            field=models.CharField(choices=[('UGX', 'UGX'), ('USD', 'USD')], default='UGX', max_length=10),
        ),
    ]
