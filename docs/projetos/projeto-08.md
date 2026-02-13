# Projeto 08 - Agenda de Contatos

## 🎯 Objetivo
Criar uma agenda telefônica simples usando um dicionário para armazenar os contatos.

## 📋 Requisitos
1. O programa deve ter um menu:
    - Adicionar Contato.
    - Buscar Contato.
    - Remover Contato.
    - Listar Todos.
    - Sair.
2. Os dados devem ser armazenados em um único dicionário onde:
    - **Chave:** Nome do contato.
    - **Valor:** Telefone do contato.

## 💡 Dicas
- Para adicionar/editar: `agenda[nome] = telefone`.
- Para buscar: `agenda.get(nome, "Não encontrado")`.
- Para remover: `agenda.pop(nome)`.
- Use `.items()` para listar tudo.

## 👣 Passo a Passo
1. Crie `agenda = {}`.
2. Implemente o loop do menu.
3. Leia a opção e execute a lógica do dicionário.
4. Teste adicionar um contato e depois buscá-lo.

## 🚀 Desafio Extra
Faça com que o valor do dicionário não seja apenas o telefone (string), mas sim outro dicionário contendo `telefone` e `email`.
Exemplo:
```python
agenda = {
    "Ricardo": {"tel": "9999-8888", "email": "ricardo@email.com"}
}
```
Atualize as funções de adicionar e buscar para lidar com essa estrutura.
