# Generated by Django 5.0.3 on 2024-07-04 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_rename_address_order_addres_alter_order_prise'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='products',
            new_name='product',
        ),
    ]
