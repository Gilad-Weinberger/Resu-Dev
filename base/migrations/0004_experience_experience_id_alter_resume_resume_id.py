# Generated by Django 4.1.13 on 2023-12-20 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_experience_just_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='experience_id',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='resume_id',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]