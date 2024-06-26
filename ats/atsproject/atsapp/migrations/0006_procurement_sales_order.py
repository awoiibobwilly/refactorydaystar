# Generated by Django 5.0.3 on 2024-05-14 08:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atsapp', '0005_checkin_checkout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_item_number', models.CharField(max_length=20)),
                ('po_product_name', models.CharField(max_length=50)),
                ('po_unit_cost', models.IntegerField()),
                ('po_purchase_date', models.DateTimeField()),
                ('po_entry_date', models.DateTimeField()),
                ('po_quantity', models.PositiveSmallIntegerField()),
                ('po_total_amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sales_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('so_date_created', models.DateTimeField()),
                ('so_unit_price', models.IntegerField()),
                ('so_quantity', models.PositiveSmallIntegerField()),
                ('so_total_amount', models.IntegerField()),
                ('so_baby_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atsapp.baby_register')),
                ('so_item_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atsapp.procurement')),
            ],
        ),
    ]
