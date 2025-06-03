from data.usuarios_db import usuarios, buscar_usuario_por_id
from quiz.controller import iniciar_quiz, mostrar_preferencias
from festa.controller import organizar_festa_via_terminal, festas_organizadas, mostrar_festa

def menu():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Criar usuário")
        print("2. Ver usuários")
        print("3. Editar usuário")
        print("4. Ver preferências (quiz respondido)")
        print("5. Responder quiz")
        print("6. Organizar festa")
        print("7. Ver festa organizada")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do usuário: ")
            novo_id = max(u["id"] for u in usuarios) + 1 if usuarios else 1
            usuarios.append({"id": novo_id, "nome": nome, "preferencias": {}})
            print(f"✅ Usuário '{nome}' criado com ID {novo_id}.")

        elif opcao == "2":
            print("\n📋 Lista de usuários:")
            for u in usuarios:
                print(f"{u['id']}: {u['nome']}")

        elif opcao == "3":
            id_str = input("Digite o ID do usuário: ")
            usuario = buscar_usuario_por_id(int(id_str))
            if usuario:
                novo_nome = input("Digite o novo nome: ")
                usuario["nome"] = novo_nome
                print("✅ Usuário atualizado com sucesso.")
            else:
                print("❌ Usuário não encontrado.")

        elif opcao == "4":
            id_str = input("Digite o ID do usuário: ")
            usuario = buscar_usuario_por_id(int(id_str))
            if usuario:
                mostrar_preferencias(usuario)
            else:
                print("❌ Usuário não encontrado.")

        elif opcao == "5":
            id_str = input("Digite o ID do usuário: ")
            usuario = buscar_usuario_por_id(int(id_str))
            if usuario:
                iniciar_quiz(usuario)
            else:
                print("❌ Usuário não encontrado.")

        elif opcao == "6":
            id_str = input("Digite o ID do usuário para organizar a festa: ")
            usuario = buscar_usuario_por_id(int(id_str))
            if usuario and usuario.get("preferencias"):
                print(f"\n🎯 Organizando festa para: {usuario['nome']}")
                organizar_festa_via_terminal(usuario)
            elif usuario:
                print("⚠️ Esse usuário ainda não respondeu o quiz.")
            else:
                print("❌ Usuário não encontrado.")

        elif opcao == "7":
            id_str = input("Digite o ID do usuário: ")
            usuario = buscar_usuario_por_id(int(id_str))
            if usuario:
                mostrar_festa(usuario)
            else:
                print("❌ Usuário não encontrado.")

        elif opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
