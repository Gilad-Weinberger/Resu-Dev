# Generated by Django 4.1.13 on 2023-12-20 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_experience_experience_id_alter_resume_resume_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='just_created',
            field=models.BooleanField(default=True),
        ),
    ]
