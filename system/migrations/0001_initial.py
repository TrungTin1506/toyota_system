# Generated by Django 5.0.6 on 2024-05-28 09:48

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('phone_number', models.IntegerField(default=0)),
                ('position', models.CharField(choices=[('Sell', 'Sell'), ('Manager', 'Manager'), ('Accountant', 'Accountant'), ('Team-Leader', 'Team-Leader')], default='', max_length=255)),
                ('working_days', models.IntegerField(blank=True, default=0, null=True)),
                ('day_off', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('slug', models.SlugField(default='', max_length=255, unique=True)),
                ('is_sub', models.BooleanField(default=False)),
                ('sub_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='system.category')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nameCar', models.CharField(default='', max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('descriptions', models.CharField(default='', max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('prioritize', models.IntegerField(default=0)),
                ('category', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='system.category')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('own_car', models.CharField(blank=True, max_length=255, null=True)),
                ('prioritize', models.IntegerField(default=0)),
                ('user_cp', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('ship_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False, null=True)),
                ('transaction_id', models.CharField(max_length=255, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('order_add', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='system.car')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.order')),
            ],
        ),
    ]
