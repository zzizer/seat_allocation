from django.db import models

class Room(models.Model):
    room_name = models.CharField(max_length=20)

    TABLES = 'Tables'
    SINGLE_SEATS = 'Single Seats'
    SELECT = 'Select'

    room_has = (
        (SELECT, 'Select'),
        (TABLES, 'Tables'),
        (SINGLE_SEATS, 'Single Seats'),
    )

    tables_or_single_seats = models.CharField(max_length=20, choices=room_has, default=SELECT)

    total_tables = models.PositiveIntegerField(default=0, blank=True, null=True)
    total_seats = models.PositiveIntegerField(default=0, blank=True, null=True)

    def room_has_tables(self):
        return self.tables_or_single_seats == self.TABLES

    def room_has_single_seats(self):
        return self.tables_or_single_seats == self.SINGLE_SEATS

    def available_table_seats(self, num_programs):
        if not self.room_has_tables():
            return None

        total_seats = self.total_tables * 3
        allocated_seats = set()

        available_seats_by_program = {}

        for program in range(1, num_programs + 1):
            available_seats = set()
            if program == 1:
                # Program 1, allocate seats to the ends of the tables, leaving the middle seat free
                for i in range(self.total_tables):
                    available_seats.update(set(range(i * 3 + 1, (i + 1) * 3 + 1, 2)) - allocated_seats)
            elif program == 2:
                # For program 2, allocate seats to the middle of the tables
                for i in range(self.total_tables):
                    available_seats.update(set(range(i * 3 + 2, (i + 1) * 3 + 1, 3)) - allocated_seats)
            elif program == 3:
                # For program 3, allocate remaining seats on the tables
                for i in range(self.total_tables):
                    remaining_seats = set(range(i * 3 + 1, (i + 1) * 3 + 1)) - allocated_seats
                    # Assign one seat per program in a round-robin manner
                    available_seats.update(list(remaining_seats)[program - 1::num_programs])

            allocated_seats.update(available_seats)
            available_seats_by_program[program] = list(available_seats)

        return available_seats_by_program

    def available_single_seats(self, num_programs):
        if not self.room_has_single_seats():
            return None

        total_seats = self.total_seats if self.total_seats is not None else 0
        total_students = num_programs  # Assuming one student per program

        if total_students > total_seats:
            raise ValueError("Not enough single seats for all students")

        # Return all available single seats
        available_seats = list(range(1, total_seats + 1))

        return available_seats

    def save(self, *args, **kwargs):
        # Dynamically set total_seats or total_tables to None based on the selected option
        if self.tables_or_single_seats == self.SELECT:
            self.total_seats = None
            self.total_tables = None
        elif self.room_has_tables():
            self.total_seats = None

        super().save(*args, **kwargs)

    def __str__(self):
        return self.room_name
