# Generated by Django 5.0.1 on 2024-01-30 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_productimage_product_prod_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
    ]
