from abc import ABC, abstractmethod
from typing import List, Dict, Any
from models import Usuario

class Observer(ABC):
    """Interface for subscribers (observers) of notifications."""
    
    @abstractmethod
    def update(self, data: Dict[str, Any]) -> None:
        """Method to be called when a subject changes state."""
        pass


class NotificationPublisher:
    """Publisher (Subject) that notifies subscribers when an event occurs."""
    
    def __init__(self):
        self._subscribers: List[Observer] = []
        
    def subscribe(self, subscriber: Observer) -> None:
        """Add a new subscriber to the notification list."""
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)
            
    def unsubscribe(self, subscriber: Observer) -> None:
        """Remove a subscriber from the notification list."""
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)
            
    def notify_all_subscribers(self, data: Dict[str, Any]) -> None:
        """Notify all subscribers about an event."""
        for subscriber in self._subscribers:
            subscriber.update(data)
    
    def get_all_subscribers(self) -> List[Observer]:
        """Get all current subscribers."""
        return self._subscribers.copy()


class EmailSubscriber(Observer):
    """Concrete subscriber that sends email notifications."""
    
    def __init__(self, usuario: Usuario):
        self.usuario = usuario
    
    def update(self, data: Dict[str, Any]) -> None:
        """Send an email notification based on received data."""
        print(f"Enviando email para {self.usuario.nome}: {data.get('mensagem', 'Sem mensagem')}")
        # Here we would actually send an email


class WhatsAppSubscriber(Observer):
    """Concrete subscriber that sends WhatsApp notifications."""
    
    def __init__(self, usuario: Usuario):
        self.usuario = usuario
    
    def update(self, data: Dict[str, Any]) -> None:
        """Send a WhatsApp message based on received data."""
        print(f"Enviando WhatsApp para {self.usuario.nome}: {data.get('mensagem', 'Sem mensagem')}")
        # Here we would actually send a WhatsApp message


class TelegramSubscriber(Observer):
    """Concrete subscriber that sends Telegram notifications."""
    
    def __init__(self, usuario: Usuario):
        self.usuario = usuario
    
    def update(self, data: Dict[str, Any]) -> None:
        """Send a Telegram message based on received data."""
        print(f"Enviando Telegram para {self.usuario.nome}: {data.get('mensagem', 'Sem mensagem')}")
        # Here we would actually send a Telegram message


# Singleton instance of the NotificationPublisher
notification_publisher = NotificationPublisher()
