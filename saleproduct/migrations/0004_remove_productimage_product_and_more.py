# Generated by Django 4.1.7 on 2023-02-16 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saleproduct', '0003_brand_product_productvariants_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productvariants',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='vaiants',
            field=models.ManyToManyField(to='saleproduct.productvariants'),
        ),
    ]