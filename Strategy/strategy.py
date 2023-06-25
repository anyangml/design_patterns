from __future__ import annotations
from abc import ABC
from abc import abstractmethod


class Character():
    
    def __init__(self) -> None:
        self._strategy = None

    @property
    def strategy(self) -> WeaponBehavior:
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy: WeaponBehavior) -> None:
        self._strategy = strategy

    def fight(self) -> None:
        self.strategy.use_weapon()
    
    def set_weapon(self, strategy: WeaponBehavior) -> None:
        self._strategy = strategy

class WeaponBehavior(ABC):
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
class King(Character):
    def __init__(self) -> None:
        self.strategy = SwordBehavior()

"""
if __name__ == "__main__":
    king = Character()
    king.strategy = SwordBehavior()
    king.fight()
    king.strategy = KnifeBehavior()
    king.fight()