import os
import django
from django.conf import settings

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

# Now you can import your models
from seat_allocation.models import Room

def test_available_seats(room, num_programs):
    available_seats = room.available_table_seats(num_programs)
    print(f"Available seats for {room.room_name} by program:")
    for program, seats in available_seats.items():
        print(f"Program {program}: {seats}")

room = Room.objects.get(room_name='R-141')
test_available_seats(room, 1)

def test_available_single_seats(room, num_programs):
    try:
        available_seats = room.available_single_seats(num_programs)
        print(f"Available single seats for {room.room_name} by program:")
        for seat in available_seats:
            print(f"Seat: {seat}")
    except ValueError as e:
        print(f"Error: {e}")

room = Room.objects.get(room_name='M4')
test_available_single_seats(room, 3)
