# Generated by Django 5.0.3 on 2024-07-01 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_rename_product_order_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address',
            new_name='addres',
        ),
        migrations.AlterField(
            model_name='order',
            name='prise',
            field=models.IntegerField(default=0),
        ),
    ]
