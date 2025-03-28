# Generated by Django 5.1.7 on 2025-03-25 11:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('diploma', models.FileField(blank=True, null=True, upload_to='diplomas/', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('image', models.ImageField(upload_to='about/')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(choices=[('static', 'Static Site'), ('business', 'Business Site'), ('webapp', 'Web App (Django)'), ('shop', 'Web Shop'), ('hr', 'HR System (custom)')], max_length=20, unique=True)),
                ('initial_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('monthly_maintenance', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.TextField()),
                ('features', models.TextField(help_text='List features separated by new lines')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('github_link', models.URLField(blank=True, null=True)),
                ('live_demo', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='projects/')),
                ('video', models.FileField(blank=True, null=True, upload_to='project_videos/', validators=[django.core.validators.FileExtensionValidator(['mp4', 'webm', 'ogg'])])),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
