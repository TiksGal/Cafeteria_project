from typing import List
from menu_items import MenuItem

class Order:
    def __init__(self) -> None:
        self.items: List[MenuItem] = []

    def add_item(self, item: MenuItem) -> None:
        self.items.append(item)

    def remove_item(self, item: MenuItem) -> None:
        self.items.remove(item)

    def update_item(self, old_item: MenuItem, new_item: MenuItem) -> None:
        index = self.items.index(old_item)
        self.items[index] = new_item

    def waiting_time(self) -> int:
        preparation_times = [item.preparation_time for item in self.items]
        max_preparation_time = max(preparation_times)
        return max_preparation_time

    def calculate_total(self) -> float:
        return sum(item.price for item in self.items)

    def add_tip(self, tip_percentage: int) -> float:
        total = self.calculate_total()
        tip_amount = total * (tip_percentage / 100)
        total_with_tip = total + tip_amount
        print(f"\nTotal with tip ({tip_percentage}%): {total_with_tip:.2f} $")
        return total_with_tip

    def generate_receipt(self, filename):
        with open(filename, "w") as file:
            file.write("Order Details:\n\n")
            for item in self.items:
                file.write(f"- {item.name} ({item.price} $)\n")
            total = self.calculate_total()
            file.write(f"\nTotal: {total} $\n")
            file.write(f"\nThank you for choosing us!")
        print(f"Receipt saved to {filename}.")


def get_order(menu: List[MenuItem]) -> Order:
    order = Order()
    while True:
        display_menu(menu)
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
    return order

def modify_order(order: Order, menu: List[MenuItem]) -> None:
    while True:
        print("\nCurrent Order:")
        for i, item in enumerate(order.items):
            print(f"{i+1}. {item}")

        option = input("Enter option number to modify or 'done' to finish modifying: ")
        if option == "done":
            break

        try:
            item = order.items[int(option) - 1]
        except (ValueError, IndexError):
            print("Invalid option. Please try again.")
            continue

        display_menu(menu)
        new_option = input("Enter new option number to replace or 'cancel' to keep the original item: ")
        if new_option == "cancel":
            continue

        try:
            new_item = menu[int(new_option) - 1]
        except (ValueError, IndexError):
            print("Invalid option. Please try again.")
            continue

        order.update_item(item, new_item)