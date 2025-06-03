from .convite_base import Convite

class DecoratorConvite(Convite):
    def __init__(self, convite: Convite):
        self._convite = convite
        super().__init__(
            destinatario=convite.destinatario,
            remetente=convite.remetente,
            titulo=convite.titulo,
            template=convite.template,
            mensagem=convite.mensagem,
            dataEnvio=convite.dataEnvio
        )

    def decorar_convite(self) -> dict:
        return self._convite.criar_convite()

    def criar_convite(self) -> dict:
        return self.decorar_convite()
