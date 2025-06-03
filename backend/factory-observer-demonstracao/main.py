from observer.subject import Festa
from observer.observers import UsuarioObserver
from factory.NotificationCreators import NotificationType

if __name__ == "__main__":
    subject =  Festa()

    usuario_1 = UsuarioObserver("Bob", [NotificationType.EMAIL, NotificationType.WHATSAPP])
    subject.attach(usuario_1)

    usuario_2 = UsuarioObserver("Alice", [NotificationType.TELEGRAM, NotificationType.WHATSAPP])
    subject.attach(usuario_2)

    subject.update_state("Mudanca de local da festa")

    subject.detach(usuario_1)
    subject.update_state("Mudanca de horario da festa")
