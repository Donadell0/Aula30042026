# Estrutura de Pastas : 
```
CodigosPython/
 ├── controller/
 │   └── usuario_controller.py
 ├── service/
 │   └── usuario_service.py
 ├── repository/
 │   └── usuario_repository.py
 ├── model/
 │   └── usuario.py
 ├── view/
 │   └── usuario_view.py
 ├── db/
 │   └── database.py
 └── main.py
```

# Diagrama de Classes (PlantUML)
<img width="334" height="539" alt="UML_DiagramaClasses" src="https://github.com/user-attachments/assets/8fb17e1b-f617-4adb-bbd2-6d9309b86fb5" />

# Diagrama de Sequência – Criar Usuário (PlantUML)
<img width="814" height="531" alt="UML_CriarUsuario" src="https://github.com/user-attachments/assets/64529eb0-68d9-4dd1-90f1-6a5b137db17b" />

# Alterações no UsuarioView

- **Menu retorna a opção**  
  Evita que o controller precise pedir input separado.

- **Uso de dicionário no menu**  
  Facilita adicionar ou remover opções.

- **Retorno em dicionário (nome/email)**  
  Mais legível e menos propenso a erro do que tupla.

- **Verificação de lista vazia**  
  Evita exibir uma lista sem conteúdo de forma confusa.

- **Mensagens com tipo (info/erro/sucesso)**  
  Melhora o feedback ao usuário.

- **Uso de `.strip()`**  
  Remove espaços desnecessários na entrada.

- **Padronização de nomes (exibir/coletar)**  
  Deixa o código mais consistente.

- **Melhor formatação visual**  
  Torna a saída mais organizada e clara.
