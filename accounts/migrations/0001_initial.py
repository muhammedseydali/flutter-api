# Generated by Django 4.1.1 on 2022-09-28 16:01

import accounts.functions
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('dob', models.DateField()),
                ('profile_picture', models.ImageField(null=True, upload_to='images/')),
                ('password', models.CharField(max_length=255)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superadmin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auto_id', models.PositiveIntegerField(db_index=True, unique=True)),
                ('type', models.CharField(max_length=255)),
                ('value', models.PositiveIntegerField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
            options={
                'verbose_name': 'image_type',
                'verbose_name_plural': 'image_types',
                'db_table': 'general_image_type',
                'ordering': ('type',),
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auto_id', models.PositiveIntegerField(db_index=True, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('model_name', models.CharField(max_length=255)),
                ('reference_id', models.UUIDField()),
                ('image', models.ImageField(upload_to=accounts.functions.get_file_path)),
                ('description', models.TextField(blank=True, null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
                ('image_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='accounts.imagetype')),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
                'db_table': 'general_image',
                'ordering': ('name',),
            },
        ),
    ]
