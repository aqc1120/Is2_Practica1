# Generated by Django 4.2.6 on 2023-12-20 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relecloud', '0004_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='email',
            field=models.EmailField(default='ifo@info.com', max_length=254),
        ),
    ]
