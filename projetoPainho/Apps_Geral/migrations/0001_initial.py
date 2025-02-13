# Generated by Django 5.0.3 on 2025-02-10 17:01

import Apps_Geral.models
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
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('ra', models.CharField(default=Apps_Geral.models.generate_unique_ra, max_length=10, unique=True)),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Admin', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('ra', models.CharField(default=Apps_Geral.models.generate_unique_ra, max_length=10, unique=True)),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Cliente', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
