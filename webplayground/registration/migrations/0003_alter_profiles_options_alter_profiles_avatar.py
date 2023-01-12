# Generated by Django 4.1.5 on 2023-01-10 18:42

from django.db import migrations, models
import registration.models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_profiles_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profiles',
            options={'ordering': ['user__username']},
        ),
        migrations.AlterField(
            model_name='profiles',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=registration.models.custom_upload_to),
        ),
    ]