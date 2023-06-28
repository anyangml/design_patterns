from __future__ import annotations
from abc import ABC, abstractmethod


class Service(ABC):
    @abstractmethod
    def request(self) -> None:
        pass


class Proxy(Service):
    _realservice: Service = None
    _allowed: set = {"admin"}

    def request(self) -> None:
        return self._realservice.request()

    def check(self, identity):

        if identity in self._allowed:
            self._realservice = RealService()
            return self.request()
        else:
            print("Not Allowed")


class RealService(Service):
    def request(self) -> None:
        print("Real Service Request")


if __name__ == "__main__":
    proxy = Proxy()
    proxy.check("admin")
    proxy.check("user")
