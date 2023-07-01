from __future__ import annotations
from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def have_next(self) -> bool:
        pass

    @abstractmethod
    def get_next(self) -> object:
        pass


class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass


class ConcreteIterator(Iterator):
    def __init__(self, aggregate: Aggregate) -> None:
        self.__aggregate = aggregate
        self.__index = 0

    def have_next(self) -> bool:
        return self.__index < len(self.__aggregate)

    def get_next(self) -> object:
        item = self.__aggregate[self.__index]
        self.__index += 1
        return item


class ConcreteAggregate(Aggregate):
    def __init__(self) -> None:
        self.__items = []

    def add(self, item: object) -> None:
        self.__items.append(item)

    def remove(self, item: object) -> None:
        self.__items.remove(item)

    def create_iterator(self) -> Iterator:
        return ConcreteIterator(self.__items)


if __name__ == "__main__":
    aggregate = ConcreteAggregate()
    aggregate.add("Item 1")
    aggregate.add("Item 2")
    aggregate.add("Item 3")
    aggregate.add("Item 4")

    iterator = aggregate.create_iterator()

    while iterator.have_next():
        print(iterator.get_next())

    print("Done")
