# Generated by Django 5.0.6 on 2024-06-13 00:08

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$')])),
                ('pin_code', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^\\d{0,9}$')])),
                ('house_no', models.CharField(max_length=300)),
                ('landmark', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='billingmodel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('name_on_card', models.CharField(blank=True, max_length=200, null=True)),
                ('customer_id', models.CharField(blank=True, max_length=200, null=True)),
                ('card_number', models.CharField(blank=True, max_length=16, null=True, unique=True)),
                ('exp_month', models.CharField(blank=True, max_length=2, null=True, validators=[django.core.validators.RegexValidator('^\\d{0,9}$')])),
                ('exp_year', models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.RegexValidator('^\\d{0,9}$')])),
                ('card_id', models.TextField(blank=True, max_length=100, null=True)),
                ('address_city', models.CharField(blank=True, max_length=120, null=True)),
                ('address_country', models.CharField(blank=True, max_length=120, null=True)),
                ('address_state', models.CharField(blank=True, max_length=120, null=True)),
                ('address_zip', models.CharField(blank=True, max_length=6, null=True, validators=[django.core.validators.RegexValidator('^\\d{0,9}$')])),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('ordered_item', models.CharField(blank=True, default='Not Set', max_length=200, null=True)),
                ('card_number', models.CharField(blank=True, max_length=16, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('paid_status', models.BooleanField(default=False)),
                ('paid_at', models.DateTimeField(blank=True, null=True)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
                ('is_delivered', models.BooleanField(default=False)),
                ('delivered_at', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
