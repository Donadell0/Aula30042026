class UsuarioView:

    def exibir_menu(self):
        opcoes = {
            "1": "Criar usuário",
            "2": "Listar usuários",
            "0": "Sair"
        }

        print("\n=== Menu ===")
        for chave, descricao in opcoes.items():
            print(f"{chave} - {descricao}")
        print("============")

        return input("Escolha uma opção: ")

    def coletar_dados_usuario(self):
        print("\n=== Novo Usuário ===")
        nome = input("Nome: ").strip()
        email = input("Email: ").strip()
        return {"nome": nome, "email": email}

    def exibir_usuarios(self, usuarios):
        print("\n=== Lista de Usuários ===")

        if not usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            for usuario in usuarios:
                print(f"[{usuario.id}] {usuario.nome} - {usuario.email}")

        print("=========================")

    def exibir_mensagem(self, mensagem, tipo="info"):
        prefixos = {
            "info": "[INFO]",
            "erro": "[ERRO]",
            "sucesso": "[OK]"
        }

        prefixo = prefixos.get(tipo, "[INFO]")
        print(f"{prefixo} {mensagem}")
