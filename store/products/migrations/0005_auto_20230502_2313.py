# Generated by Django 3.2.13 on 2023-05-02 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_products_basket_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'категории', 'verbose_name_plural': 'категории'},
        ),
    ]
