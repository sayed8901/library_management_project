# Generated by Django 4.2.4 on 2024-06-29 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0008_activity_is_returned'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='is_returned',
        ),
        migrations.AddField(
            model_name='activity',
            name='status',
            field=models.CharField(default='active', max_length=10),
        ),
    ]
