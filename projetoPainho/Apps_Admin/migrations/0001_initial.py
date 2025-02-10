# Generated by Django 5.0.3 on 2025-02-10 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=20)),
                ('especialidade', models.TextField(max_length=1000)),
                ('crm', models.CharField(max_length=10)),
                ('estado', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('endereco', models.TextField(max_length=500)),
                ('telefone', models.CharField(max_length=20)),
                ('especialidade', models.TextField(max_length=1000)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=2)),
            ],
        ),
    ]
