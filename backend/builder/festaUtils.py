from builder import Festa

# Classe para utilitários relacionados à Festa
class FestaUtils:
    @staticmethod
    def gerarConvite(festa: Festa) -> str:
        """
        Gera um convite formatado com base nos dados da festa.
        """
        convite = f"""
        ================================
               CONVITE PARA A FESTA
        ================================
        🎉 Nome do Aniversariante: {festa.nomeAniversariante}
        📍 Local: {festa.local}
        📅 Data: {festa.data.strftime('%d/%m/%Y')}
        ⏰ Hora: {festa.hora.strftime('%H:%M')}
        🔗 Link do Grupo: {festa.linkGrupo if festa.linkGrupo else 'Não informado'}
        ================================
        """
        return convite

    @staticmethod
    def gerarPreferencias(festa: Festa) -> str:
        """
        Gera as preferências formatadas com base nos dados da festa.
        """
        preferencias = f"""
        ================================
           PREFERÊNCIAS DA FESTA
        ================================
        🍴 Buffet: {', '.join(festa.buffet)}
        🎵 Estilos Musicais: {', '.join(festa.estilosMusicais)}
        ================================
        """
        return preferencias