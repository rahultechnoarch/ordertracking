# Generated by Django 3.2.6 on 2021-08-27 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_update_statustext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update',
            name='statustext',
            field=models.CharField(choices=[('Your Order is Received', 'Your Order is Received'), ('Your Order is In Transit', 'Your Order is In Transit'), ('Your Order is Out for Delivery', 'Your Order is Out for Delivery'), ('Your Order is Delivered', 'Your Order is Delivered')], default='Order Received', max_length=50),
        ),
    ]
