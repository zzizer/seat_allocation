# Generated by Django 5.0.1 on 2024-01-20 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seat_allocation', '0003_alter_room_tables_or_single_seats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='total_seats',
        ),
    ]
