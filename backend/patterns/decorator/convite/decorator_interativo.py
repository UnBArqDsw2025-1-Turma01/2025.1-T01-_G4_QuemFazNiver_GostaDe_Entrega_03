from .decorator_base import DecoratorConvite

class DecoratorInterativo(DecoratorConvite):
    def __init__(self, convite):
        super().__init__(convite)
        self.googleMaps = None
        self.carousel = []
        self.comentarios = []

    def configurar_mapa(self, latitude: float, longitude: float, zoom: int = 15):
        self.googleMaps = {
            "latitude": latitude,
            "longitude": longitude,
            "zoom": zoom
        }

    def adicionar_imagem_carousel(self, image_url: str):
        self.carousel.append({"tipo": "imagem", "url": image_url})

    def adicionar_comentario(self, comentario: str):
        self.comentarios.append(comentario)

    def decorar_convite(self) -> dict:
        convite_base = super().decorar_convite()

        interativo = {}
        if self.googleMaps:
            interativo["googleMaps"] = self.googleMaps

        if self.carousel:
            interativo["carousel"] = self.carousel

        if self.comentarios:
            interativo["comentarios"] = self.comentarios

        if interativo:
            convite_base["interativo"] = interativo

        return convite_base

    def confirmar_convite(self):
        self.set_status("CONFIRMADO")