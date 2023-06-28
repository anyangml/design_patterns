from __future__ import annotations
from abc import ABC
from abc import abstractmethod


class Character:
    def __init__(self) -> None:
        self._weapon: WeaponBehavior = None

    def fight(self) -> None:
        self._weapon.use_weapon()

    def set_weapon(self, weapon: WeaponBehavior) -> None:
        self._weapon = weapon


class WeaponBehavior(ABC):
    """
    This is an interface
    """

    @abstractmethod
    def use_weapon(self) -> None:
        pass


class KnifeBehavior(WeaponBehavior):
    def use_weapon(self) -> None:
        print("Using knife")


class SwordBehavior(WeaponBehavior):
    def use_weapon(self) -> None:
        print("Using sword")


"""
This would be the concret class of abstract class Character, 
if polymorphism is used.

class King(Character):
    def __init__(self) -> None:
        self.strategy = SwordBehavior()
"""

if __name__ == "__main__":
    king = Character()
    king.set_weapon(SwordBehavior())
    king.fight()
    king.set_weapon(KnifeBehavior())
    king.fight()
