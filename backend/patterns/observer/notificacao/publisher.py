from typing import List
from .usuario import Usuario
from patterns.factory_method.notification import NotificationService 

class NotificationPublisher:
    """Publisher (Subject) that notifies subscribers when an event occurs."""
    
    def __init__(self):
        self._subscribers: List[Usuario] = []
        
    def subscribe(self, subscriber: Usuario) -> None:
        """Add a new subscriber to the notification list."""
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)
            
    def unsubscribe(self, subscriber: Usuario) -> None:
        """Remove a subscriber from the notification list."""
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)
            
    def notify_all_subscribers(self) -> None:
        """Notify all subscribers about an event."""
        for subscriber in self._subscribers:
            for tipo in subscriber.tiposDeNotificacao: 
                NotificationService(tipo).notify(subscriber.nome, "Evento notificado")
    
    def get_all_subscribers(self) -> List[Usuario]:
        """Get all current subscribers."""
        return self._subscribers.copy()


notification_publisher = NotificationPublisher()
