# Generated by Django 5.0.2 on 2024-02-26 19:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_experience_just_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='degree',
            name='education_year',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
