# Generated by Django 4.1.7 on 2023-02-16 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraddressbook',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='useraddressbook',
            name='last_name',
        ),
        migrations.AddField(
            model_name='useraddressbook',
            name='receiver_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
