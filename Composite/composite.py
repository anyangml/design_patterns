from __future__ import annotations
from abc import ABC, abstractmethod


class MenuComponent(ABC):
    def add(self) -> None:
        pass

    def remove(self) -> None:
        pass

    def getChild(self) -> MenuComponent:
        pass

    def getPrice(self) -> float:
        pass


class Menu(MenuComponent):
    def __init__(self) -> None:
        self.menuComponents = []

    def add(self, menuComponent: MenuComponent) -> None:
        self.menuComponents.append(menuComponent)

    def remove(self, menuComponent: MenuComponent) -> None:
        self.menuComponents.remove(menuComponent)

    def getChild(self, i: int) -> MenuComponent:
        return self.menuComponents[i]


class MenuItem(MenuComponent):
    def __init__(self, price: float) -> None:
        self.price = price

    def getPrice(self) -> float:
        return self.price


if __name__ == "__main__":
    lunc_menu = Menu()
    tuna_wrap = MenuItem(5.0)
    fries = MenuItem(3.0)
    lunc_menu.add(tuna_wrap)
    lunc_menu.add(fries)
    print(lunc_menu.getChild(0).getPrice())
