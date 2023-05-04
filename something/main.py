from restaurant import Restaurant
from models import Order, Reservation
import datetime

class App:
    def __init__(self):
        self.restaurant = Restaurant()

    def run(self):
        print("Hello, nice to meet you!")
        reservation_answer = input("Do you already make a reservation? Yes/No: ")

        if reservation_answer.lower() == "yes":
            name = input("Please enter your name: ")
            date = input("Please enter reservation date (YYYY-MM-DD): ")
            date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            reservation = self.restaurant.find_reservation(name, date)

            if reservation is None:
                print("Sorry, we can't find a reservation for this person.")

        new_reservation_answer = input("Would you like to make a new reservation? Yes/No: ")

        if new_reservation_answer.lower() == "yes":
            name = input("Please enter your name: ")
            date = input("Please enter reservation date (YYYY-MM-DD): ")
            date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            new_reservation = Reservation(name, date)
            self.restaurant.add_reservation(new_reservation)
            print("Congrats! You have booked a table!")

            table_answer = input("Would you like to take a table now? Yes/No: ")

            if table_answer.lower() == "yes":
                self.restaurant.show_menu()
                order = self.process_order()
                print(f"\nTotal price: ${order.calculate_total():.2f}")
                tip_percentage = int(input("\nEnter tip percentage: "))
                order.add_tip(tip_percentage)
                receipt_filename = "receipt.txt"
                order.generate_receipt(receipt_filename)
                print("Thank you for choosing us! Have a great day!")
            else:
                print("Thank you for choosing us! Have a great day!")

    def process_order(self):
        order = Order()
        while True:
            item_name = input("Enter the name of the menu item you'd like to order, or type 'done' to finish: ")

            if item_name.lower() == 'done':
                break

            found = False
            for item in self.restaurant.menu:
                if item.name.lower() == item_name.lower():
                    order.add_item(item)
                    print(f"{item.name} added to your order.")
                    found = True
                    break

            if not found:
                print("Menu item not found. Please try again.")

        return order
    


if __name__ == "__main__":
    app = App()
    app.run()