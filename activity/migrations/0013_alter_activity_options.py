# Generated by Django 4.2.4 on 2024-06-29 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0012_activity_balance_after_activity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ['created_on']},
        ),
    ]
