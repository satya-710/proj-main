# Generated by Django 5.0.1 on 2024-02-15 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anynomous', '0002_user_master'),
    ]

    operations = [
        migrations.CreateModel(
            name='test_employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=20, unique=True)),
                ('contact', models.CharField(blank=True, max_length=12)),
                ('image', models.ImageField(upload_to='images')),
                ('address', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updates_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
