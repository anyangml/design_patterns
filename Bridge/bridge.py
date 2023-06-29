from __future__ import annotations
from abc import ABC, abstractmethod

class Display(ABC):

    def __init__(self, resource: Resource) -> None:
        self.resource = resource

    @abstractmethod
    def show(self) -> None:
        pass

class Resource(ABC):
    @abstractmethod
    def summary(self) -> str:
        pass

class WebDisplay(Display):
    def show(self) -> None:
        print(f'WebDisplay: {self.resource.summary()}')

class PhoneDisplay(Display):
    def show(self) -> None:
        print(f'PhoneDisplay: {self.resource.summary()}')

class NovelResource(Resource):
    def summary(self) -> str:
        return 'Novel'
    
class FictionResource(Resource):
    def summary(self) -> str:
        return 'Fiction'
    
if __name__ == '__main__':
    novel = NovelResource()
    fiction = FictionResource()

    web_display = WebDisplay(novel)
    phone_display = PhoneDisplay(fiction)

    web_display.show()
    phone_display.show()