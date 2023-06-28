from __future__ import annotations
from abc import ABC, abstractmethod


class Publisher(ABC):
    @abstractmethod
    def add_subscriber(self, subscriber: Subscriber) -> None:
        pass

    @abstractmethod
    def remove_subscriber(self, subscriber: Subscriber) -> None:
        pass

    @abstractmethod
    def publish(self) -> None:
        pass


class Subscriber(ABC):
    @abstractmethod
    def update(self, publisher: Publisher) -> None:
        pass


class CNN(Publisher):
    _subscribers = []
    _latest_news = None

    def add_subscriber(self, subscriber: Subscriber) -> None:
        self._subscribers.append(subscriber)

    def remove_subscriber(self, subscriber: Subscriber) -> None:
        self._subscribers.remove(subscriber)

    def publish(self) -> None:
        for subscriber in self._subscribers:
            subscriber.update(self)

    # This is the business logic
    def set_latest_news(self, latest_news: str) -> None:
        self._latest_news = latest_news
        self.publish()


"""
The following classes are the subscribers implemented in a 'pull' manner, 
alternatively, the subscribers could be implemented in a 'push' manner.
If the '_latest_news' is passed as a parameter to the 'update' method, the
concrete subscriber class would be able to access the '_latest_news' variable
without accessing the 'CNN' class.
"""


class GoldTier(Subscriber):
    def update(self, publiser: CNN) -> None:
        print(f"Hi Gold Member, the latest news is {publiser._latest_news}")


class SilverTier(Subscriber):
    def update(self, publiser: CNN) -> None:
        print(f"Hi Silver Member, the latest news is {publiser._latest_news}")


if __name__ == "__main__":
    cnn = CNN()
    userA = GoldTier()
    userB = SilverTier()
    cnn.add_subscriber(userA)
    cnn.add_subscriber(userB)
    cnn.set_latest_news("The latest news is: 'The world is going to end today.'")
    cnn.remove_subscriber(userA)
    cnn.set_latest_news("The latest news is: 'The world is going to end tomorrow.'")
