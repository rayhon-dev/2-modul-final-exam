# Generated by Django 5.1.6 on 2025-02-14 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_alter_group_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='academic_year',
            field=models.CharField(max_length=100),
        ),
    ]
