from models import Reservation, MenuItem, BreakfastMenuItem, LunchMenuItem, DinnerMenuItem, AlcoholFreeMenuItem, AlcoholMenuItem, VegetarianMenuItem, VeganMenuItem

class Restaurant:
    def __init__(self):
        self.reservations = []
        self.tables = {
            'family': 5,
            'single': 10,
            'double': 7,
        }
        self.menu = [
            BreakfastMenuItem("Eggs Benedict", 200, 15, 500, 15.99),
            LunchMenuItem("Caesar Salad", 250, 10, 300, 12.99),
            DinnerMenuItem("Steak with Mashed Potatoes", 400, 25, 800, 29.99),
            AlcoholFreeMenuItem("Orange Juice", 250, 5, 100, 4.99),
            AlcoholMenuItem("Red Wine", 750, 10, 200, 19.99),
            VegetarianMenuItem("Stir Fry Vegetables", 300, 20, 400, 15.99),
            VeganMenuItem("Vegan Burger", 250, 15, 350, 12.99),
        ]

    def find_reservation(self, name, date):
        for reservation in self.reservations:
             if reservation.name.lower() == name.lower() and reservation.date == date:
                return reservation
        return None

    def add_reservation(self, reservation):
        self.reservations.append(reservation)

    def show_menu(self):
        print("\nMENU:")
        for item in self.menu:
            print(item)