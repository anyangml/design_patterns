from __future__ import annotations
from abc import ABC, abstractmethod


class Client:
    def __init__(self, taget: Target) -> None:
        self.target = taget


class Target(ABC):
    @abstractmethod
    def request(self) -> str:
        pass


class Adaptee:
    def processed_request(self) -> str:
        return "processed request"


class Adapter(Target):
    def __init__(self, adaptee: Adaptee) -> None:
        self._adaptee = adaptee

    def request(self) -> str:
        return self._adaptee.processed_request()


if __name__ == "__main__":
    client = Client(Adapter(Adaptee()))
    print(client.target.request())
