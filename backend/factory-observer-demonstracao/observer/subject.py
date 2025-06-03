from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def attach(self, observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

    @abstractmethod
    def get_state(self) -> str:
        pass


# Concrete subject class
class Festa(Subject):
    _message_state = ""
    _observers = []

    def get_state(self):
        return self._message_state

    def attach(self, observer) -> None:
        self._observers.append(observer)

    def detach(self, observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def update_state(self, state: str):
        self._message_state = state
        self.notify()
