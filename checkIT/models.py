import datetime
from dataclasses import dataclass, field
from typing import List

@dataclass
class Reservation:
    name: str
    date: datetime.date

    def __str__(self):
        return f'{self.name} on {self.date}'

class MenuItem:
    def __init__(self, name, serving_size, prep_time, calories, price):
        self.name = name
        self.serving_size = serving_size
        self.prep_time = prep_time
        self.calories = calories
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price}"

class BreakfastMenuItem(MenuItem):
    pass

class LunchMenuItem(MenuItem):
    pass

class DinnerMenuItem(MenuItem):
    pass

class AlcoholFreeMenuItem(MenuItem):
    pass

class AlcoholMenuItem(MenuItem):
    pass

class VegetarianMenuItem(MenuItem):
    pass

class VeganMenuItem(MenuItem):
    pass

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
        preparation_times = [item.prep_time for item in self.items]
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