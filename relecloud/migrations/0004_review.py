# Generated by Django 4.2.6 on 2023-10-18 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relecloud', '0003_cruise'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('review', models.TextField(max_length=2000)),
            ],
        ),
    ]
