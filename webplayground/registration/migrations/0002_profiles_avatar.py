# Generated by Django 4.1.5 on 2023-01-07 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='profiles'),
        ),
    ]
