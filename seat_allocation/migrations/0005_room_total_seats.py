# Generated by Django 5.0.1 on 2024-01-20 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seat_allocation', '0004_remove_room_total_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='total_seats',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
