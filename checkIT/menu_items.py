from abc import ABC, abstractmethod

class MenuItem(ABC):
    def __init__(
        self, name: str, weight: int, preparation_time: int, calories: int, price: float
    ):
        self.name = name
        self.weight = weight
        self.preparation_time = preparation_time
        self.calories = calories
        self.price = price

    @abstractmethod
    def get_menu_type(self) -> str:
        pass


class BreakfastMenuItem(MenuItem):
    def get_menu_type(self) -> str:
        return "Breakfast"


class LunchMenuItem(MenuItem):
    def get_menu_type(self) -> str:
        return "Lunch"


class DinnerMenuItem(MenuItem):
    def get_menu_type(self) -> str:
        return "Dinner"


class DrinkMenuItem(MenuItem):
    def get_menu_type(self) -> str:
        return "Drink"


class AlcoholMenuItem(DrinkMenuItem):
    def get_menu_type(self) -> str:
        return "Alcohol"


class AlcoholFreeMenuItem(DrinkMenuItem):
    def get_menu_type(self) -> str:
        return "Alcohol-Free"


class VegetarianMenuItem(MenuItem):
    def get_menu_type(self) -> str:
        return "Vegetarian"


class VeganMenuItem(MenuItem):
    def get_menu_type(self) -> str:
        return "Vegan"