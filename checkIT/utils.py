import datetime
from typing import List
from menu_items import MenuItem

def display_menu(menu: List[MenuItem]) -> None:
    print("\nMenu:")
    for i, item in enumerate(menu):
        print(f"{i+1}. {item}")
        
def get_user_information() -> dict:
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    reservation_time = input("Enter reservation time (YYYY-MM-DD HH:MM): ")

    user_info = {
        "first_name": first_name,
        "last_name": last_name,
        "reservation_time": reservation_time,
    }
    return user_info

def display_welcome_message(user_info: dict, table_number: int) -> None:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"Welcome {user_info['first_name']}, {user_info['last_name']} to our restaurant")
    print(f"Current time is: {current_time}")
    print("You do not have a reservation")
    print(f"{user_info['first_name']}, {user_info['last_name']} your table is: {table_number} reserved at {user_info['reservation_time']} o'clock")
