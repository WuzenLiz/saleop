# Generated by Django 4.1.7 on 2023-02-16 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_userinfomation_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfomation',
            name='address',
        ),
        migrations.AlterField(
            model_name='useraddressbook',
            name='phone',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfomation',
            name='phone',
            field=models.CharField(default='', max_length=100),
        ),
    ]
