# Generated by Django 5.1.6 on 2025-02-12 18:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0003_alter_department_status'),
        ('teachers', '0002_teacher_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='head_of_department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='departments', to='teachers.teacher'),
        ),
    ]
