# Generated by Django 4.2.4 on 2024-06-28 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.useraccount'),
        ),
    ]
