from abc import ABC, abstractmethod

class Template(ABC):
    def basemethod(self):
        print("base method")

    def hook(self):
        print("hook method in Template")

    @abstractmethod
    def abstractmethod(self):
        pass

class ConcreteOne(Template):
    def abstractmethod(self):
        print("concrete one")

class ConcreteTwo(Template):
    def abstractmethod(self):
        print("concrete two")

    def hook(self):
        print("hook method in concrete two")


if __name__ == "__main__":
    one = ConcreteOne()
    one.basemethod()
    one.abstractmethod()
    one.hook()

    two = ConcreteTwo()
    two.basemethod()
    two.abstractmethod()
    two.hook()