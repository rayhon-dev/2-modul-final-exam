# Generated by Django 5.1.6 on 2025-02-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('on_leave', 'On Leave')], default='active', max_length=10),
        ),
    ]
