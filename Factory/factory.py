from __future__ import annotations
from abc import ABC, abstractmethod

class Factory(ABC):
    @abstractmethod
    def build_product(self) -> Product:
        pass

class Product(ABC):
    @abstractmethod
    def show(self) -> None:
        pass

class AncientFactory(Factory):
    def build_product(self) -> Product:
        return AncientProduct()

class MordenFactory(Factory):
    def build_product(self) -> Product:
        return MordenProduct()

class AncientProduct(Product):
    def show(self) -> None:
        print("AncientProduct")

class MordenProduct(Product):
    def show(self) -> None:
        print("MordenProduct")

if __name__ == "__main__":
    ancient_factory = AncientFactory()
    ancient_product = ancient_factory.build_product()
    ancient_product.show()

    morden_factory = MordenFactory()
    morden_product = morden_factory.build_product()
    morden_product.show()