# Generated by Django 4.1.7 on 2023-02-17 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saleproduct', '0013_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='description',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='meta_keywords',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='subcategory_icon',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='subcategory_image',
        ),
    ]
