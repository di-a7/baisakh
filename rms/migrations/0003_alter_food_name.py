# Generated by Django 5.2.3 on 2025-06-30 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0002_table_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
