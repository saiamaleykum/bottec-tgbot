# Generated by Django 5.0.6 on 2024-06-05 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'managed': False},
        ),
    ]