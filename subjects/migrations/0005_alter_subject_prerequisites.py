# Generated by Django 5.1.6 on 2025-02-13 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0004_subject_levels_alter_subject_prerequisites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='prerequisites',
            field=models.CharField(max_length=100),
        ),
    ]
