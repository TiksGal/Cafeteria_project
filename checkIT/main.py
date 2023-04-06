from menu_items import (
    BreakfastMenuItem,
    LunchMenuItem,
    DinnerMenuItem,
    AlcoholFreeMenuItem,
    AlcoholMenuItem,
    VegetarianMenuItem,
    VeganMenuItem,
)
from orders import Order, get_order, modify_order
from table import (
    Table,
    Reservation,
    initialize_tables,
    display_tables,
    select_table,
    get_reservations,
    check_reservation_exists,
)
from utils import display_menu, get_user_information, display_welcome_message
import datetime

def main():
    initialize_tables()
    reservation_list = get_reservations()

    display_tables()
    user_info = get_user_information()
    table = select_table(user_info['first_name'] + " " + user_info['last_name'], user_info['reservation_time'])

    display_welcome_message(user_info, table.table_number)

    for reservation in reservation_list:
        matching_tables = [
            table
            for table in table
            if table.table_type == reservation.table_type and not table.reserved
        ]
        if matching_tables:
            table = matching_tables[0]
            table.reserved = True
            table.reservation_name = reservation.name
            table.reservation_time = datetime.datetime.strptime(
                reservation.reservation_time, "%Y-%m-%d %H:%M"
            )
            print(
                f"Table {table.table_number} ({table.table_type}) is reserved for {table.reservation_name} at {table.reservation_time}."
            )
        else:
            print(
                f"No available table of type {reservation.table_type} for {reservation.name} at {reservation.reservation_time}."
            )

    display_tables()
    table = select_table()
    
    user_info = get_user_information()
    display_welcome_message(user_info, table.table_number)

    menu = [
        BreakfastMenuItem("Eggs Benedict", 200, 15, 500, 15.99),
        LunchMenuItem("Caesar Salad", 250, 10, 300, 12.99),
        DinnerMenuItem("Steak with Mashed Potatoes", 400, 25, 800, 29.99),
        AlcoholFreeMenuItem("Orange Juice", 250, 5, 100, 4.99),
        AlcoholMenuItem("Red Wine", 750, 10, 200, 19.99),
        VegetarianMenuItem("Stir Fry Vegetables", 300, 20, 400, 15.99),
        VeganMenuItem("Vegan Burger", 250, 15, 350, 12.99),
    ]

    order = Order()
    while True:
        print("\nMenu:")
        for i, item in enumerate(menu):
            print(f"{i+1}. {item.name} - {item.price} $")

        option = input("Enter option number to order or 'done' to finish ordering: ")
        if option == "done":
            break

        try:
            item = menu[int(option) - 1]
        except (ValueError, IndexError):
            print("Invalid option. Please try again.")
            continue

        order.add_item(item)
        print(f"{item.name} added to order.")

    print("\nOrder:")
    for item in order.items:
        print(f"- {item.name} ({item.price} $)")

    while True:
        modify = input("Do you want to modify the order? (yes/no): ")
        if modify == "no":
            break

        print("\nCurrent Order:")
        for i, item in enumerate(order.items):
            print(f"{i+1}. {item.name} ({item.price} $)")

        try:
            option = int(
                input("Enter option number to modify or 'done' to finish modifying: ")
            )
        except ValueError:
            print("Invalid option. Please try again.")
            continue

        if option == "done":
            break

        try:
            item = order.items[option - 1]
        except IndexError:
            print("Invalid option. Please try again.")
            continue

        new_option = input(
            "Enter new option number to replace or 'cancel' to keep the original item: "
        )
        if new_option == "cancel":
            continue

        try:
            new_item = menu[int(new_option) - 1]
        except (ValueError, IndexError):
            print("Invalid option. Please try again.")
            continue

        order.update_item(item, new_item)

    total = order.calculate_total()
    print(f"\nTotal: {total} $")

    add_tip = input("Do you want to add a tip? (yes/no): ")
    if add_tip.lower() == "yes":
        tip_percentage = int(input("Enter tip percentage: "))
        total_with_tip = order.add_tip(tip_percentage)
        print(f"\nTotal with tip ({tip_percentage}%): {total_with_tip} $")
    else:
        total_with_tip = total

    print("\nOrder:")
    for item in order.items:
        print(f"- {item.name} ({item.price} $)")

    print(f"\nTotal with tip ({tip_percentage}%): {total_with_tip} $")
    print(f"Approximate waiting time: {order.waiting_time()} minutes.")

    order.generate_receipt("order.txt")
    print("Thank you for dining with us!")


if __name__ == "__main__":
    main()
