# Generated by Django 5.0.6 on 2024-06-05 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_cart_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cart',
            table='Cart',
        ),
        migrations.AlterModelTable(
            name='category',
            table='Category',
        ),
        migrations.AlterModelTable(
            name='item',
            table='Item',
        ),
        migrations.AlterModelTable(
            name='order',
            table='Order',
        ),
        migrations.AlterModelTable(
            name='orderitem',
            table='OrderItem',
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]