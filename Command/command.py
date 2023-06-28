from __future__ import annotations
from abc import ABC, abstractmethod


class Invoker:
    commandA: Command = None
    commandB: Command = None


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class ConcreteCommandA(Command):
    def __init__(self, receiver: ConcreteReceiver) -> None:
        self.receiver = receiver

    def execute(self) -> None:
        self.receiver.actionA()

    def undo(self) -> None:
        self.receiver.undoA()


class ConcreteCommandB(Command):
    def __init__(self, receiver: ConcreteReceiver) -> None:
        self.receiver = receiver

    def execute(self) -> None:
        self.receiver.actionB()

    def undo(self) -> None:
        self.receiver.undoB()


class ConcreteReceiver:
    def actionA(self) -> None:
        print("Action A")

    def actionB(self) -> None:
        print("Action B")

    def undoA(self) -> None:
        print("Undo A")

    def undoB(self) -> None:
        print("Undo B")


if __name__ == "__main__":
    invoker = Invoker()
    receiver = ConcreteReceiver()
    invoker.commandA = ConcreteCommandA(receiver)
    invoker.commandB = ConcreteCommandB(receiver)
    invoker.commandA.execute()
    invoker.commandB.execute()
    invoker.commandA.undo()
    invoker.commandB.undo()
