from .base_quiz import QuizTemplate

class QuizPreferenciasTerminal(QuizTemplate):
    def fazer_perguntas(self):
        perguntas = {
                        "lugares": [
                            "Praia", "Campo", "Parque", "Cinema", "Boate", "Restaurante", "Casa de amigos",
                            "Clube", "Cobertura com vista", "Chácara", "Balada temática", "Piquenique no parque"
                        ],
                        "comidas": [
                            "Pizza", "Churrasco", "Sushi", "Hambúrguer", "Tábua de frios", "Docinhos de festa",
                            "Espetinhos", "Massas (lasanha, macarronada)", "Comida mexicana", "Cachorro-quente",
                            "Salgadinhos variados", "Sorvete e milk-shake"
                        ],
                        "musicas": [
                            "Sertanejo", "Rock", "Funk", "MPB", "Pop", "Eletrônica", "Axé", "Pagode",
                            "Brega funk", "Trap", "Forró", "K-pop", "Anos 2000", "Reggaeton"
                        ]
                    }

        respostas = {}

        for categoria, opcoes in perguntas.items():
            print(f"\n{categoria.capitalize()} que você gostaria no seu aniversário:")
            for i, opcao in enumerate(opcoes, 1):
                print(f"{i}. {opcao}")
            entrada = input("Escolha os números separados por vírgula: ")
            selecionados = [opcoes[int(i.strip()) - 1] for i in entrada.split(",") if i.strip().isdigit()]
            respostas[categoria] = selecionados

        return respostas

    def salvar_preferencias(self, usuario, respostas):
        usuario["preferencias"] = respostas