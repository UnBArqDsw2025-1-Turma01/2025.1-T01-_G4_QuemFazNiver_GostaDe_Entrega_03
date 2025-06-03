from .decorator_base import DecoratorConvite

class DecoratorLuxo(DecoratorConvite):
    def __init__(self, convite):
        super().__init__(convite)
        self.carousel = []
        self.videos = []
        self.sons = None
        self.tipografia = "Arial"

    def adicionar_video(self, video_url: str):
        self.videos.append(video_url)

    def configurar_som(self, som_url: str, autoplay: bool = False):
        self.sons = {
            "url": som_url,
            "autoplay": autoplay
        }

    def configurar_tipografia(self, fonte: str):
        self.tipografia = fonte

    def adicionar_imagem_carousel(self, image_url: str):
        self.carousel.append(image_url)

    def decorar_convite(self) -> dict:
        convite_base = super().decorar_convite()

        luxo = {}
        if self.carousel:
            luxo["carousel"] = self.carousel

        if self.videos:
            luxo["videos"] = self.videos

        if self.sons:
            luxo["sons"] = self.sons

        if self.tipografia:
            luxo["tipografia"] = self.tipografia

        if luxo:
            convite_base["luxo"] = luxo

        return convite_base