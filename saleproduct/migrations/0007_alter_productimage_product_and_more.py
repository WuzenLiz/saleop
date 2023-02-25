# Generated by Django 4.1.7 on 2023-02-16 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saleproduct', '0006_productimage_product_productvariants_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='saleproduct.product'),
        ),
        migrations.AlterField(
            model_name='productvariants',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='saleproduct.product'),
        ),
    ]
