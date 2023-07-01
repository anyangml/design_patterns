from __future__ import annotations
from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle_request(self) -> None:
        pass

class OnState(State):
    def handle_request(self) -> None:
        print("On")

class OffState(State):
    def handle_request(self) -> None:
        print("Off")

class TV(ABC):
    def __init__(self) -> None:
        self._state = None
    def set_state(self, state: State) -> None:
        self._state = state
    
    def operate(self) -> None:
        self._state.handle_request()

if __name__ == "__main__":
    tv = TV()
    on_state = OnState()
    off_state = OffState()
    tv.set_state(on_state)
    tv.operate()
    tv.set_state(off_state)
    tv.operate()