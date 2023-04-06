from typing import List

class Table:
    def __init__(self, table_type: str, table_number: int):
        self.table_type = table_type
        self.table_number = table_number
        self.reserved = False
        self.reservation_name = None
        self.reservation_time = None
        

class Reservation:
    def __init__(self, name: str, table_type: str, reservation_time: str):
        self.name = name
        self.table_type = table_type
        self.reservation_time = reservation_time


table_types = {
    "Single": 10,
    "Double": 6,
    "Family": 4,
}

tables = []
reservation_list = []


def initialize_tables():
    table_number = 1
    for table_type, count in table_types.items():
        for i in range(count):
            table = Table(table_type, table_number)
            if i < 2:
                table.reserved = True
                table.reservation_name = f"Reserved-{table_number}"
            tables.append(table)
            table_number += 1


def display_tables() -> None:
    available_tables = []
    reserved_tables = []
    for table in tables:
        if table.reserved:
            reserved_tables.append(table)
        else:
            available_tables.append(table)

    print("Available Tables:")
    for table in available_tables:
        print(f"Table {table.table_number} ({table.table_type})")

    print("\nReserved Tables:")
    for table in reserved_tables:
        print(
            f"Table {table.table_number} ({table.table_type}) - {table.reservation_name}"
        )


def select_table(reservation_name=None, reservation_time=None) -> Table:
    while True:
        table_number = int(input("Enter table number: "))
        table = tables[table_number - 1]
        if not table.reserved:
            if reservation_name and reservation_time:
                table.reserved = True
                table.reservation_name = reservation_name
                table.reservation_time = reservation_time
            return table
        else:
            print("Table is already reserved. Please select another table")
            
def get_reservations() -> List[Reservation]:
    reservations = []
    while True:
        reserved = input("Is a table reserved? (yes/no): ").lower()
        if reserved == "yes":
            name = input("Enter reservation name: ")
            table_type = input("Enter table type: ")
            reservation_time = input("Enter reservation time (YYYY-MM-DD HH:MM): ")
            
            if check_reservation_exists(reservation_time, table_type):
                print("There is already a reservation for this time and table type.")
            else:
                reservation = Reservation(name, table_type, reservation_time)
                reservations.append(reservation)
        else:
            break
    return reservations

def check_reservation_exists(reservation_time: str, table_type: str) -> bool:
    for reservation in reservation_list:
        if reservation.reservation_time == reservation_time and reservation.table_type == table_type:
            return True
    return False

