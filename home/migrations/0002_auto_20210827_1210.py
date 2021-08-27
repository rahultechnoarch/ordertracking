# Generated by Django 3.2.6 on 2021-08-27 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Order Received', 'Order Received'), ('Order Scheduled', 'Order Scheduled'), ('Shipped Out', 'Shipped Out'), ('Arrived at warehouse', 'Arrived at warehouse'), ('Out for Delivery', 'Out for Delivery'), ('Order Delivered', 'Order Delivered')], default='In Progress', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='update_Time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
