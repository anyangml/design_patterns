from __future__ import annotations
from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass


class AddonDecorator(Beverage, ABC):
    def __init__(self, beverage: Beverage) -> None:
        self._beverage = beverage

    @abstractmethod
    def cost(self) -> float:
        pass


class Tea(Beverage):
    def cost(self) -> float:
        price = 3.0
        return price


class Coffee(Beverage):
    def cost(self) -> float:
        price = 4.0
        return price


class Milk(AddonDecorator):
    def cost(self) -> float:
        new_price = self._beverage.cost() + 0.5
        return new_price


class Sugar(AddonDecorator):
    def cost(self) -> float:
        new_price = self._beverage.cost() + 0.5
        return new_price


if __name__ == "__main__":
    tea = Tea()
    milk_tea = Milk(tea)
    milk_tea_with_suger = Sugar(milk_tea)
    print(f" The final price is {milk_tea_with_suger.cost()}")

    coffee = Coffee()
    coffee_with_suger = Sugar(coffee)
    print(f" The final price is {coffee_with_suger.cost()}")
