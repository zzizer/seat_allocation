# Generated by Django 5.0.1 on 2024-01-20 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seat_allocation', '0002_alter_room_tables_or_single_seats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='tables_or_single_seats',
            field=models.CharField(choices=[('Select', 'Select'), ('Tables', 'Tables'), ('Single Seats', 'Single Seats')], default='Select', max_length=20),
        ),
    ]
