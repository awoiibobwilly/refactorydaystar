# Generated by Django 5.0.3 on 2024-05-11 18:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atsapp', '0004_alter_sitter_register_sit_nin_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin_sitter_availability', models.CharField(choices=[('On Duty', 'On Duty'), ('Off Duty', 'Off Duty')], max_length=10)),
                ('checkin_time', models.TimeField()),
                ('checkin_date', models.DateField()),
                ('checkin_care_time', models.CharField(choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening'), ('Night', 'Night')], max_length=10)),
                ('checkin_guardians_sur_name', models.CharField(max_length=100)),
                ('checkin_guardians_other_names', models.CharField(max_length=200)),
                ('checkin_guardians_telephone', models.IntegerField()),
                ('checkin_payment_choice', models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')], max_length=10)),
                ('daystar_checkin_fee', models.IntegerField()),
                ('daystar_checkin_fee_currency', models.CharField(default='UGX', max_length=10)),
                ('checkin_comment', models.CharField(max_length=1000)),
                ('baby_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atsapp.baby_register')),
                ('sitter_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atsapp.sitter_register')),
            ],
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkout_time', models.TimeField()),
                ('checkout_date', models.DateField()),
                ('checkout_care_time', models.CharField(choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening'), ('Night', 'Night')], max_length=10)),
                ('checkout_guardians_sur_name', models.CharField(max_length=100)),
                ('checkout_guardians_other_names', models.CharField(max_length=200)),
                ('checkout_guardians_telephone', models.IntegerField()),
                ('checkout_payment_choice', models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')], max_length=10)),
                ('daystar_care_time_fee', models.IntegerField()),
                ('daystar_care_time_fee_currency', models.CharField(default='UGX', max_length=10)),
                ('checkout_sitter_fee', models.IntegerField()),
                ('checkout_sitter_fee_currency', models.CharField(default='UGX', max_length=10)),
                ('checkout_comment', models.CharField(max_length=1000)),
                ('baby_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atsapp.baby_register')),
                ('sitter_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atsapp.sitter_register')),
            ],
        ),
    ]
