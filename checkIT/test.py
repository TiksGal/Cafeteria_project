import pickle
from dataclasses import dataclass, field
from typing import List

table_types = {
    "Single": 10,
    "Double": 6,
    "Family": 4,
}

tables = []
reservation_list = []

RESERVATIONS_FILE = "reservations.pickle"


@dataclass
class Table:
    table_type: str
    table_number: int
    reserved: bool = field(default=False)


@dataclass
class Reservation:
    name: str
    table_type: str
    reservation_time: str


def initialize_tables():
    table_number = 1
    for table_type, count in table_types.items():
        for i in range(count):
            table = Table(table_type, table_number)
            tables.append(table)
            table_number += 1


def display_tables() -> None:
    available_tables = tables.copy()
    reserved_tables = []
    for reservation in reservation_list:
        matching_tables = [
            table
            for table in tables
            if table.table_type == reservation.table_type
            and table not in reserved_tables
        ]
        if matching_tables:
            reserved_table = matching_tables[0]
            reserved_tables.append(reserved_table)
            available_tables.remove(reserved_table)

    print("Available Tables:")
    for table in available_tables:
        print(f"Table {table.table_number} ({table.table_type})")

    print("\nReserved Tables:")
    for reservation, table in zip(reservation_list, reserved_tables):
        print(
            f"Table {table.table_number} ({table.table_type}) - {reservation.name} at {reservation.reservation_time}"
        )


def save_reservations():
    with open(RESERVATIONS_FILE, "wb") as file:
        pickle.dump(reservation_list, file)


def load_reservations():
    try:
        with open(RESERVATIONS_FILE, "rb") as file:
            reservations = pickle.load(file)
    except FileNotFoundError:
        reservations = []
    return reservations


def check_reservation(name: str, table_type: str, reservation_time: str) -> Reservation:
    for reservation in reservation_list:
        if (
            reservation.name.lower() == name.lower()
            and reservation.table_type.lower() == table_type.lower()
            and reservation.reservation_time == reservation_time
        ):
            return reservation
    return None

def main():
    initialize_tables()
    global reservation_list
    reservation_list = load_reservations()

    print("Welcome to the restaurant reservation system!")

    while True:
        action = input("What would you like to do? (reserve/check/display/exit): ").lower()

        if action == "reserve":
            name = input("Enter reservation name: ")
            table_type = input("Enter table type: ").capitalize()
            reservation_time = input("Enter reservation time (YYYY-MM-DD HH:MM): ")

            reservation = Reservation(name, table_type, reservation_time)

            matching_tables = [
                table
                for table in tables
                if table.table_type == reservation.table_type and not table.reserved
            ]
            if matching_tables:
                table = matching_tables[0]
                print(
                    f"Table {table.table_number} ({table.table_type}) is reserved for {reservation.name} at {reservation.reservation_time}."
                )

                reservation_list.append(reservation)
                save_reservations()
            else:
                print(
                    f"No available table of type {reservation.table_type} for {reservation.name} at {reservation.reservation_time}."
                )

        elif action == "check":
            name = input("Enter reservation name: ")
            table_type = input("Enter table type: ").capitalize()
            reservation_time = input("Enter reservation time (YYYY-MM-DD HH:MM): ")

            reservation = check_reservation(name, table_type, reservation_time)
            if reservation:
                print(
                    f"Reservation found: {reservation.name} - {reservation.table_type} table at {reservation.reservation_time}."
                )
            else:
                print("No reservation found with the provided details.")

        elif action == "display":
            display_tables()

        elif action == "exit":
            print("Thank you for using the reservation system!")
            break

if __name__ == "__main__":
    main()




           



